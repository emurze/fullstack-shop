import abc

from seedwork.models import AggregateRoot as AgRoot


class IGenericRepository[Model: AgRoot, ModelId: int](metaclass=abc.ABCMeta):
    model_class: Model

    @abc.abstractmethod
    def add(self, model: Model) -> ModelId: ...

    @abc.abstractmethod
    def delete(self, model: Model) -> None: ...

    @abc.abstractmethod
    def get_by_id(
        self,
        ido: ModelId,
        for_update: bool = False,
    ) -> Model | None: ...

    @abc.abstractmethod
    def count(self) -> int: ...


class GenericRepository[Model: AgRoot, ModelId: int](IGenericRepository):
    model_class: Model

    def add(self, model: Model) -> ModelId:
        model.save()
        return model.id

    def delete(self, model: Model) -> None:
        model.delete()

    def get_by_id(
        self,
        ido: ModelId,
        for_update: bool = False,
    ) -> Model | None:
        query = self.model_class.objects

        if for_update:
            query = query.select_for_update()

        return query.filter(id=ido).first()

    def count(self) -> int:
        return self.model_class.objects.count()
