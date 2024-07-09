import abc
import logging
from typing import Self

from django.db import transaction

from seedwork.repositories import IGenericRepository


class IUnitOfWork(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __enter__(self) -> Self: ...

    @abc.abstractmethod
    def __exit__(self, *args) -> None: ...

    @abc.abstractmethod
    def commit(self) -> None: ...

    @abc.abstractmethod
    def rollback(self) -> None: ...


class DjangoUnitOfWork(IUnitOfWork):  # TODO: add logging
    def __init__(self, *repositories: IGenericRepository) -> None:
        self.lg = logging.getLogger()
        self.repositories = repositories

    def __enter__(self) -> Self:
        transaction.set_autocommit(False)
        return self

    def __exit__(self, *args) -> None:
        self.rollback()
        transaction.set_autocommit(True)

    def _persist(self) -> None:
        for repo in self.repositories:
            for model in repo.seen:
                model.save()

    def commit(self) -> None:
        self.lg.debug("COMMIT")
        self._persist()
        transaction.commit()

    def rollback(self):
        self.lg.debug("ROLLBACK")
        transaction.rollback()
