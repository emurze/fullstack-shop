import abc


class IGenericRepository[Model, ModelId](metaclass=abc.ABCMeta):
    model_class: Model
    seen: set

    @abc.abstractmethod
    def add(self, model: Model) -> ModelId: ...

    @abc.abstractmethod
    def delete_by_id(self, ido: ModelId) -> None: ...

    @abc.abstractmethod
    def get_by_id(
        self,
        ido: ModelId,
        for_update: bool = False,
    ) -> Model | None: ...

    @abc.abstractmethod
    def count(self) -> int: ...


class GenericRepository[Model, ModelId](IGenericRepository):
    model_class: Model

    def __init__(self) -> None:
        self.seen = set()

    def add(self, model: Model) -> ModelId:
        model.full_clean()
        model.save()
        return model.id

    def delete_by_id(self, ido: ModelId) -> None:
        self.model_class.objects.filter(id=ido).delete()

    def get_by_id(
        self,
        ido: ModelId,
        for_update: bool = False,
    ) -> Model | None:
        query = self.model_class.objects

        if for_update:
            query = query.select_for_update()

        model = query.filter(id=ido).first()
        self.seen.add(model)
        return model

    def count(self) -> int:
        return self.model_class.objects.count()
