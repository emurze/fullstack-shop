from dataclasses import dataclass

import pytest
from faker import Faker
from injector import Injector

from seedwork.exceptions import (
    MissingFirstArgumentAnnotationException,
    HandlerDoesNotHaveMessageException,
)
from seedwork.mediator import Mediator
from seedwork.uows import DjangoUnitOfWork


@pytest.fixture(scope="function")
def mediator() -> Mediator:
    uow = DjangoUnitOfWork()
    container = Injector()
    mediator = Mediator(uow, container=container)
    container.binder.bind(Mediator, to=mediator)
    return mediator


class NullTestMessage:
    pass


class SayHelloTestMessage:
    def __init__(self, title_: str) -> None:
        self.title = title_


class NotificationTestService:
    @staticmethod
    def say_hello(message: SayHelloTestMessage) -> str:
        return f"<{message.title}>"

    def write(self, _: NullTestMessage) -> str:
        return f"Write {type(self).__name__}"


@dataclass(frozen=True)
class OrderPizzaTestMessage:
    title: str


@dataclass(frozen=True)
class OrderTestService:
    mediator: Mediator

    def order_pizza(self, command: OrderPizzaTestMessage) -> tuple[str, str]:
        result = self.mediator.basic_handle(SayHelloTestMessage(command.title))
        return result, f"({command.title})"


@pytest.mark.unit
def test_can_register_two_services(mediator: Mediator) -> None:
    # act
    mediator.register_service(NotificationTestService)
    mediator.register_service(OrderTestService)


@pytest.mark.unit
def test_can_handle_empty_message(mediator: Mediator) -> None:
    # arrange
    mediator.register_service(NotificationTestService)

    # act
    res2 = mediator.basic_handle(NullTestMessage())

    # assert
    assert res2 == f"Write {NotificationTestService.__name__}"


@pytest.mark.unit
def test_service_can_call_another_service(
    mediator: Mediator,
    faker: Faker,
) -> None:
    # arrange
    mediator.register_service(NotificationTestService)
    mediator.register_service(OrderTestService)

    # act
    title = faker.text(max_nb_chars=30)
    res = mediator.basic_handle(OrderPizzaTestMessage(title))

    # assert
    assert res == (f"<{title}>", f"({title})")


@pytest.mark.unit
def test_can_register_handler(mediator: Mediator, faker: Faker) -> None:
    # arrange
    @dataclass(frozen=True)
    class SayHelloCommand:
        message: str

    def say_hello(command: SayHelloCommand) -> str:
        return f"<{command.message}>"

    mediator.register_handler(say_hello)

    # act
    message = faker.text(max_nb_chars=30)
    res = mediator.basic_handle(SayHelloCommand(message=message))

    # assert
    assert res == f"<{message}>"


@pytest.mark.unit
def test_cannot_register_service_without_argument(mediator: Mediator) -> None:
    # arrange
    def verify_client() -> None:
        print("Client is verified")

    # act
    with pytest.raises(HandlerDoesNotHaveMessageException):
        mediator.register_handler(verify_client)


@pytest.mark.unit
def test_cannot_register_handler_without_argument_annotation(
    mediator: Mediator,
) -> None:
    # arrange
    def send_credentials_to_client(command) -> None:
        print(f"Client notified by <{command.message}>")

    # act
    with pytest.raises(MissingFirstArgumentAnnotationException):
        mediator.register_handler(send_credentials_to_client)
