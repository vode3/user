from app.domain.user.entities import User as UserEntity
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
from app.infrastructure.persistence.models import UserModel


def convert_user_entity_to_db_model(user: UserEntity) -> UserModel:
    return UserModel(
        id=user.id.raw_value,
        first_name=user.first_name.raw_value,
        last_name=user.last_name.raw_value,
        username=user.username.raw_value,
        email=user.email.raw_value,
        password=user.password.raw_value,
        role=user.role.raw_value,
        created_at=user.created_at.raw_value,
        updated_at=user.updated_at.raw_value,
        deleted_at=user.deleted_at.raw_value,
    )


def convert_user_db_model_to_entity(user: UserModel) -> UserEntity:
    return UserEntity(
        id=UserId(user.id),
        first_name=FirstName(user.first_name),
        last_name=LastName(user.last_name),
        username=Username(user.username),
        email=Email(user.email),
        password=HashedPassword(user.password),
        role=Role(user.role),
        created_at=CreatedAt(user.created_at),
        updated_at=UpdatedAt(user.updated_at),
        deleted_at=DeletedAt(user.deleted_at),
    )
