from typing import Optional, Sequence

from sqlalchemy import select

from app.domain.user.entities import User
from app.domain.user.interfaces.persistence.reader import UserReader
from app.domain.user.value_objects import Email, UserId, Username
from app.infrastructure.persistence.converters.user import (
    convert_user_db_model_to_entity,
)
from app.infrastructure.persistence.models import UserModel
from app.infrastructure.persistence.repositories.base import SQLAlchemyGateway


class SQLAlchemyUserReader(SQLAlchemyGateway, UserReader):
    async def get_by_id(self, user_id: UserId) -> User:
        stmt = select(UserModel).where(UserModel.id == user_id.raw_value)
        user: Optional[UserModel] = (await self._session.execute(stmt)).scalars().first()

        if not user:
            raise Exception("User not found")

        return convert_user_db_model_to_entity(user)

    async def get_by_email(self, email: Email) -> User:
        stmt = select(UserModel).where(UserModel.email == email.raw_value)
        user: Optional[UserModel] = (await self._session.execute(stmt)).scalars().first()
        if not user:
            raise Exception("User not found")

        return convert_user_db_model_to_entity(user)

    async def get_by_username(self, username: Username) -> User:
        stmt = select(UserModel).where(UserModel.username == username.raw_value)
        user: Optional[UserModel] = (await self._session.execute(stmt)).scalars().first()
        if not user:
            raise Exception("User not found")

        return convert_user_db_model_to_entity(user)

    async def get_all(self, limit: int, offset: int) -> Sequence[User]:
        stmt = select(UserModel).limit(limit).offset(offset)
        users: Sequence[UserModel] = (await self._session.execute(stmt)).scalars().all()
        if not users:
            raise Exception("No users found")

        return [convert_user_db_model_to_entity(user) for user in users]
