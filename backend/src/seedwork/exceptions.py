from collections.abc import Callable
from dataclasses import dataclass


@dataclass(eq=False)
class ServiceException(Exception):
    @property
    def message(self):
        return "Service error occurred"


@dataclass(eq=False)
class CommandHandlerNotRegisteredException(ServiceException):
    command_type: type

    @property
    def message(self) -> str:
        return f"Command handler is not registered for {self.command_type}"


@dataclass(eq=False)
class HandlerDoesNotHaveMessageException(ServiceException):
    func: Callable

    @property
    def message(self) -> str:
        return (
            f"Command handler {self.func.__name__} doesn't have any commands"
        )


@dataclass(eq=False)
class MissingFirstArgumentAnnotationException(ServiceException):
    func: Callable

    @property
    def message(self) -> str:
        return (
            f"Missing first argument annotation for command of "
            f"{self.func.__name__}"
        )
