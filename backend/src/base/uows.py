import abc
import logging
from typing import Self

from django.db import transaction

from base.repositories import IGenericRepository


class IUnitOfWork(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __enter__(self) -> Self: ...

    @abc.abstractmethod
    def __exit__(self, *args) -> None: ...

    @abc.abstractmethod
    def persist(self) -> None: ...

    @abc.abstractmethod
    def commit(self) -> None: ...

    @abc.abstractmethod
    def rollback(self) -> None: ...


class DjangoUnitOfWork(IUnitOfWork):
    def __init__(self, *repositories: IGenericRepository) -> None:
        self.logger = logging.getLogger()
        self.repositories = repositories

    def __enter__(self) -> Self:
        transaction.set_autocommit(False)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        if exc_type is None:
            self.commit()
        else:
            self.rollback()
        transaction.set_autocommit(True)

    def persist(self) -> None:
        for repo in self.repositories:
            for model in repo.seen:
                model.save()

    def commit(self) -> None:
        self.persist()
        self.logger.debug("COMMIT")
        transaction.commit()

    def rollback(self):
        self.logger.debug("ROLLBACK")
        transaction.rollback()
