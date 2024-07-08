from dataclasses import dataclass
from typing import Any

import pytest
from faker import Faker
from injector import Injector

from seedwork.exceptions import (
    HandlerDoesNotHaveCommandsException,
    ServiceDoesNotHaveInitMethodException,
    MissingFirstArgumentAnnotationException,
    CommandIsNotDataClassException,
)
from seedwork.mediator import Mediator, command_handler
from seedwork.uows import DjangoUnitOfWork


@dataclass(frozen=True)
class IChatService:
    @command_handler
    def add_message_to_client(self, command: Any) -> None:
        print(f"Add message <{command}> to a client")


class TInventoryService:
    pass


class TNotificationService:
    def __init__(self) -> None:
        pass

    @command_handler
    def notify_client_about_credentials(self) -> None:
        print("Notify client about credentials")


@dataclass(frozen=True)
class IDeliveryService:
    @command_handler
    def notify_client_about_credentials(self, command) -> None:
        print(f"Deliver things to a client from {command=}")


@dataclass(frozen=True)
class TCreateProductCommand:
    title: str


@dataclass(frozen=True)
class TUpdateProductCommand:
    title: str


@dataclass(frozen=True)
class TProductService:
    mediator: Mediator

    @command_handler
    def create_product(self, command: TCreateProductCommand) -> str:
        return f"Product {command.title} created"

    @command_handler
    def update_product(self, command: TUpdateProductCommand) -> str:
        return f"Product {command.title} updated"


@dataclass(frozen=True)
class TCreateOrderCommand:
    name: str
    product_id: int


@dataclass(frozen=True)
class TOrderService:
    mediator: Mediator

    @command_handler
    def create_order(self, command: TCreateOrderCommand) -> tuple[str, str]:
        res = self.mediator.handle(TCreateProductCommand(title=command.name))
        return res, f"Order {command.name} created"


@pytest.mark.integration
@pytest.mark.django_db(transaction=True)
class TestMediator:
    def setup_class(self) -> None:
        uow = DjangoUnitOfWork()
        container = Injector()
        mediator = Mediator(uow=uow, container=container)
        container.binder.bind(Mediator, to=mediator)

        self.mediator = mediator
        self.faker = Faker()

    def test_can_register_command(self) -> None:
        self.mediator.register_service_commands(TProductService)

        title = self.faker.text(max_nb_chars=50)
        command = TCreateProductCommand(title=title)
        res = self.mediator.handle(command)

        command2 = TUpdateProductCommand(title=title)
        res2 = self.mediator.handle(command2)

        assert res == f"Product {command.title} created"
        assert res2 == f"Product {command2.title} updated"

    def test_can_register_two_services(self) -> None:
        self.mediator.register_service_commands(TProductService)
        self.mediator.register_service_commands(TOrderService)

        name = self.faker.text(max_nb_chars=50)
        command = TCreateOrderCommand(name=name, product_id=1)
        res1, res2 = self.mediator.handle(command)

        assert res1 == f"Product {command.name} created"
        assert res2 == f"Order {command.name} created"

    def test_cannot_register_service_without_init(self) -> None:
        with pytest.raises(ServiceDoesNotHaveInitMethodException):
            self.mediator.register_service_commands(TInventoryService)

    def test_cannot_register_service_without_command(self) -> None:
        with pytest.raises(HandlerDoesNotHaveCommandsException):
            self.mediator.register_service_commands(TNotificationService)

    def test_cannot_register_service_without_command_annotation(self) -> None:
        with pytest.raises(MissingFirstArgumentAnnotationException):
            self.mediator.register_service_commands(IDeliveryService)

    def test_cannot_register_service_with_wrong_annotation(self) -> None:
        with pytest.raises(CommandIsNotDataClassException):
            self.mediator.register_service_commands(IChatService)
