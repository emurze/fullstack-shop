import inspect
from collections.abc import Callable
from dataclasses import dataclass, field
from typing import Any, TypeAlias

from injector import Injector, inject

from seedwork.exceptions import (
    CommandHandlerNotRegisteredException,
    HandlerDoesNotHaveMessageException,
    MissingFirstArgumentAnnotationException,
)
from seedwork.uows import IUnitOfWork

Message: TypeAlias = Any


def get_first_argument_annotation(func: Callable) -> Any:
    signature = inspect.signature(func)
    parameters = list(signature.parameters.values())

    if not parameters:
        raise HandlerDoesNotHaveMessageException(func)

    first_param = parameters[0]
    annotation = first_param.annotation

    # noinspection PyProtectedMember
    # noinspection PyUnresolvedReferences
    if annotation is inspect._empty:
        raise MissingFirstArgumentAnnotationException(func)

    return annotation


@dataclass(frozen=True)
class Mediator:
    # TODO: Integrate celery in mediator
    # EACH DELIVERY TASK SHOULD HAVE OWN TRANSACTION

    uow: IUnitOfWork
    container: Injector
    message_map: dict[type[Message], Callable] = field(default_factory=dict)

    def register_handler(self, handler: Callable) -> None:
        message_type = get_first_argument_annotation(handler)
        self.message_map[message_type] = handler

    def register_service(self, service_class: Any) -> None:
        try:
            service = self.container.get(inject(service_class))
        except AttributeError:
            service = service_class()

        functions = inspect.getmembers(service, inspect.isfunction)
        methods = inspect.getmembers(service, inspect.ismethod)
        all_functions = functions + methods

        for method_name, method in all_functions:
            if not method_name.startswith("_"):
                self.register_handler(method)

    def handle(self, message: Message) -> Any:
        handler = self._get_handler(message)

        with self.uow:
            # if is celery adapter
            handler.delay(message)

            res = handler(message)
            self.uow.commit()
            return res

    def basic_handle(self, message: Message) -> Any:
        handler = self._get_handler(message)
        return handler(message)

    def _get_handler(self, message: Message) -> Callable:
        message_type = type(message)
        handler = self.message_map[message_type]

        if not handler:
            raise CommandHandlerNotRegisteredException(message_type)

        return handler
