import abc
from typing import Self

from django.db import transaction


class IUnitOfWork(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __enter__(self) -> Self: ...

    @abc.abstractmethod
    def __exit__(self, *args) -> None: ...

    @abc.abstractmethod
    def commit(self) -> None: ...

    @abc.abstractmethod
    def rollback(self) -> None: ...


class DjangoUnitOfWork(IUnitOfWork):
    def __enter__(self):
        transaction.set_autocommit(False)
        return super().__enter__()

    def __exit__(self, *args):
        self.rollback()
        transaction.set_autocommit(True)

    def commit(self):
        transaction.commit()

    def rollback(self):
        transaction.rollback()
