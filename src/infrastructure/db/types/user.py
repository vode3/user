import datetime
import uuid
from typing import Optional

from sqlalchemy import DateTime, Enum, Text
from sqlalchemy.dialects.postgresql import UUID

from src.domain.user.value_objects import (
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
from src.infrastructure.db.types.base import BaseType


class IDType(BaseType[uuid.UUID]):
    impl = UUID(as_uuid=True)
    cache_ok = True
    _vo = UserId


class FirstNameType(BaseType[str]):
    impl = Text
    _vo = FirstName


class LastNameType(BaseType[str]):
    impl = Text
    _vo = LastName


class UsernameType(BaseType[str]):
    impl = Text
    cache_ok = True
    _vo = Username


class HashedPasswordType(BaseType[str]):
    impl = Text
    _vo = HashedPassword


class EmailType(BaseType[str]):
    impl = Text
    cache_ok = True
    _vo = Email


class RoleType(BaseType[RoleEnum]):
    impl = Enum(RoleEnum, name="role_enum")
    _vo = Role


class CreatedAtType(BaseType[datetime.datetime]):
    impl = DateTime(timezone=True)
    _vo = CreatedAt


class UpdatedAtType(BaseType[datetime.datetime]):
    impl = DateTime(timezone=True)
    _vo = UpdatedAt


class DeletedAtType(BaseType[Optional[datetime.datetime]]):
    impl = DateTime(timezone=True)
    _vo = DeletedAt
