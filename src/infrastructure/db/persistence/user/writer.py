from src.domain.user.entities import User as UserEntity
from src.domain.user.interfaces.persistence.writer import UserWriter
from src.domain.user.value_objects import UserId
from src.infrastructure.db.persistence.base import SQLAlchemyGateway


class SQLAlchemyUserWriter(SQLAlchemyGateway, UserWriter): ...


# test.py
from datetime import datetime
from typing import Optional
from uuid import uuid4

from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from src.domain.user.value_objects import (  # noqa: E402
    CreatedAt,
    DeletedAt,
    Email,
    FirstName,
    HashedPassword,
    LastName,
    Role,
    UpdatedAt,
    UserId,
    Username,
)
from src.domain.user.value_objects.role import RoleEnum
from src.infrastructure.config import load_settings


from src.domain.user.entities import User
from src.infrastructure.db.models.base import mapper_registry, metadata
from src.infrastructure.db.models.user import user_table


__all__ = (
    "metadata",
    "user_table",
)

# mapper_registry.map_imperatively(User, user_table)


def async_engine() -> AsyncEngine:
    return create_async_engine(load_settings().db.url)


def create_session_factory(
    engine: Optional[AsyncEngine] = None,
) -> async_sessionmaker[AsyncSession]:
    if engine is None:
        engine = async_engine()

    return async_sessionmaker(engine, autoflush=False, expire_on_commit=False)


def async_session(
    session_factory: Optional[async_sessionmaker[AsyncSession]] = None,
) -> AsyncSession:
    if session_factory is None:
        session_factory = create_session_factory()
    return session_factory()


async def main() -> None:
    session = async_session()
    creation_time = datetime.utcnow()
    user = UserEntity(
        id=UserId(uuid4()),
        email=Email("vd3@proton.me"),
        first_name=FirstName("Vlad"),
        last_name=LastName("Dracula"),
        password=HashedPassword("vlad"),
        role=Role(RoleEnum.ADMIN),
        created_at=CreatedAt(creation_time),
        updated_at=UpdatedAt(creation_time),
        deleted_at=DeletedAt(None),
        username=Username("vlad1"),
    )
    from uuid import UUID

    session.add(user)
    await session.commit()
    print(await session.get(UserEntity, UserId(UUID("a4ae8be6-7e76-4967-9ae9-e4d77754808e"))))


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
