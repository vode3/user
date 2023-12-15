from sqlalchemy import Column, Table

from src.infrastructure.db.models.base import metadata
from src.infrastructure.db.types.user import (
    CreatedAtType,
    DeletedAtType,
    EmailType,
    FirstNameType,
    HashedPasswordType,
    IDType,
    LastNameType,
    RoleType,
    UpdatedAtType,
    UsernameType,
)


user_table = Table(
    "user",
    metadata,
    Column("id", IDType, primary_key=True, index=True),
    Column("first_name", FirstNameType),
    Column("last_name", LastNameType),
    Column("username", UsernameType, unique=True, index=True),
    Column("email", EmailType, unique=True, index=True),
    Column("password", HashedPasswordType),
    Column("role", RoleType, default="user"),
    Column("created_at", CreatedAtType),
    Column("updated_at", UpdatedAtType),
    Column("deleted_at", DeletedAtType, nullable=True),
)
