from dataclasses import dataclass

from app.domain.common.entities.base import Entity
from app.domain.user.value_objects import (
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
from app.domain.user.value_objects.role import RoleEnum


@dataclass
class User(Entity[UserId]):
    id: UserId
    first_name: FirstName
    last_name: LastName
    email: Email
    username: Username
    password: HashedPassword
    role: Role
    created_at: CreatedAt
    updated_at: UpdatedAt
    deleted_at: DeletedAt

    @property
    def is_admin(self) -> bool:
        return self.role.raw_value == RoleEnum.ADMIN

    @property
    def is_deleted(self) -> bool:
        return self.deleted_at.raw_value is not None
