import inspect
from collections.abc import Callable
from dataclasses import is_dataclass
from typing import Any, TypeAlias

from injector import Injector, inject

from seedwork.exceptions import (
    CommandHandlerNotRegisteredException,
    HandlerDoesNotHaveCommandsException,
    MissingFirstArgumentAnnotationException,
    ServiceDoesNotHaveInitMethodException,
    CommandIsNotDataClassException,
)
from seedwork.uows import IUnitOfWork

Command: TypeAlias = Any


def command_handler[TF](func: TF) -> TF:
    func._is_command_handler = True
    return func


# TODO: provide behavior for static methods
def get_first_argument_annotation(func: Callable) -> Any:
    signature = inspect.signature(func)
    parameters = list(signature.parameters.values())

    if not parameters:
        raise HandlerDoesNotHaveCommandsException(func)

    first_param = parameters[0]
    annotation = first_param.annotation

    # noinspection PyProtectedMember
    # noinspection PyUnresolvedReferences
    if annotation is inspect._empty:
        raise MissingFirstArgumentAnnotationException(func)

    if not is_dataclass(annotation):
        raise CommandIsNotDataClassException(func)

    return annotation


class BasicMediator:
    container: Injector
    command_map: dict[type[Command], Callable]

    def __init__(
        self,
        container: Injector,
        command_map: dict | None = None,
    ) -> None:
        self.container = container
        self.command_map = {} if command_map is None else command_map

    def register_command(
        self,
        command_type: type[Command],
        _command_handler: Callable,
    ) -> None:
        self.command_map[command_type] = _command_handler

    def register_service_commands(self, service_type: Any) -> None:
        try:
            service = self.container.get(inject(service_type))
        except AttributeError:
            raise ServiceDoesNotHaveInitMethodException(service_type)

        methods = inspect.getmembers(service, inspect.ismethod)

        for _, method in methods:
            if not hasattr(method, "_is_command_handler"):
                continue

            command_type = get_first_argument_annotation(method)
            self.register_command(command_type, method)

    @staticmethod
    def execute_handler(handler: Callable, command: Command) -> Any:
        return handler(command)

    def handle(self, command: Command) -> Any:
        command_type = type(command)
        handler = self.command_map[command_type]

        if not handler:
            raise CommandHandlerNotRegisteredException(command_type)

        return self.execute_handler(handler, command)


class Mediator(BasicMediator):
    def __init__(self, container: Injector, uow: IUnitOfWork) -> None:
        super().__init__(container)
        self.uow = uow

    def execute_handler(self, handler: Callable, command: Command) -> Any:
        with self.uow:
            res = handler(command)
            self.uow.commit()
            return res
