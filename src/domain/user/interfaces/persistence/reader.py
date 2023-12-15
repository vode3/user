from abc import ABC, abstractmethod
from typing import List

from src.domain.user.entities import User
from src.domain.user.value_objects import Email, UserId, Username


class UserReader(ABC):
    @abstractmethod
    async def get_by_id(self, user_id: UserId) -> User:
        raise NotImplementedError

    @abstractmethod
    async def get_by_email(self, email: Email) -> User:
        raise NotImplementedError

    @abstractmethod
    async def get_by_username(self, username: Username) -> User:
        raise NotImplementedError

    @abstractmethod
    async def get_all(self, limit: int, offset: int) -> List[User]:
        raise NotImplementedError
