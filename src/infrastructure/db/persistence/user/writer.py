from sqlalchemy import insert, update

from src.domain.user.entities import User
from src.domain.user.interfaces.persistence.writer import UserWriter
from src.infrastructure.db.models.user import user_table
from src.infrastructure.db.persistence.base import SQLAlchemyGateway


class SQLAlchemyUserWriter(SQLAlchemyGateway, UserWriter):
    async def create(self, user: User) -> None:
        stmt = insert(User).values(**user.to_dict())
        await self._session.execute(stmt)

    async def update(self, user: User) -> None:
        stmt = update(User).where(user_table.c.id == user.id).values(**user.to_dict())
        await self._session.execute(stmt)
