from sqlalchemy import insert, update

from app.domain.user.entities import User
from app.domain.user.interfaces.persistence.writer import UserWriter
from app.infrastructure.persistence.converters.user import (
    convert_user_entity_to_db_model,
)
from app.infrastructure.persistence.models import UserModel
from app.infrastructure.persistence.repositories.base import SQLAlchemyGateway


class SQLAlchemyUserWriter(SQLAlchemyGateway, UserWriter):
    async def create(self, user: User) -> None:
        user_model = convert_user_entity_to_db_model(user)

        stmt = insert(UserModel).values(**user_model.__dict__)
        await self._session.execute(stmt)

    async def update(self, user: User) -> None:
        user_model = convert_user_entity_to_db_model(user)

        stmt = update(UserModel).where(UserModel.id == user.id).values(**user_model.__dict__)
        await self._session.execute(stmt)
