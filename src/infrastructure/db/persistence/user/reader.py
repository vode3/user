from typing import Optional, Sequence

from sqlalchemy import select

from src.domain.user.entities import User
from src.domain.user.interfaces.persistence.reader import UserReader
from src.domain.user.value_objects import Email, UserId, Username
from src.infrastructure.db.models.user import user_table
from src.infrastructure.db.persistence.base import SQLAlchemyGateway


class SQLAlchemyUserReader(SQLAlchemyGateway, UserReader):
    async def get_by_id(self, user_id: UserId) -> User:
        stmt = select(User).where(user_table.c.id == user_id)
        user: Optional[User] = (await self._session.execute(stmt)).scalars().first()
        if not user:
            raise Exception("User not found")
        return user

    async def get_by_email(self, email: Email) -> User:
        stmt = select(User).where(user_table.c.email == email)
        user: Optional[User] = (await self._session.execute(stmt)).scalars().first()
        if not user:
            raise Exception("User not found")
        return user

    async def get_by_username(self, username: Username) -> User:
        stmt = select(User).where(user_table.c.username == username)
        user: Optional[User] = (await self._session.execute(stmt)).scalars().first()
        if not user:
            raise Exception("User not found")
        return user

    async def get_all(self, limit: int, offset: int) -> Sequence[User]:
        stmt = select(User).limit(limit).offset(offset)
        users: Sequence[User] = (await self._session.execute(stmt)).scalars().all()
        if not users:
            raise Exception("No users found")
        return users
