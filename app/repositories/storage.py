from abc import ABC, abstractmethod


class Repositories(ABC):

    @abstractmethod
    async def get_by_id(self, pk: int):
        """Получаем объект по pk."""

    @abstractmethod
    async def get_multy(self):
        """Получаем несколько объектов."""

    @abstractmethod
    async def update_object(self, obj):
        """Обновление объекта."""
