from abc import ABC, abstractmethod

from app.domain.user.entities import User


class UserWriter(ABC):
    @abstractmethod
    async def create(self, user: User) -> None:
        raise NotImplementedError

    @abstractmethod
    async def update(self, user: User) -> None:
        raise NotImplementedError
