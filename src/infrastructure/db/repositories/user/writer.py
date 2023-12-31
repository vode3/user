from sqlalchemy import insert, update

from src.domain.user.entities import User
from src.domain.user.interfaces.persistence.writer import UserWriter
from src.infrastructure.db.converters.user import convert_user_entity_to_db_model
from src.infrastructure.db.models import User as UserModel
from src.infrastructure.db.repositories.base import SQLAlchemyGateway


class SQLAlchemyUserWriter(SQLAlchemyGateway, UserWriter):
    async def create(self, user: User) -> None:
        user_model = convert_user_entity_to_db_model(user)

        stmt = insert(UserModel).values(**user_model.__dict__)
        await self._session.execute(stmt)

    async def update(self, user: User) -> None:
        user_model = convert_user_entity_to_db_model(user)

        stmt = update(UserModel).where(UserModel.id == user.id).values(**user_model.__dict__)
        await self._session.execute(stmt)
