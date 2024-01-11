from dataclasses import dataclass
from enum import Enum

from app.domain.common.value_objects import ValueObject


class RoleEnum(Enum):
    ADMIN = "admin"
    USER = "user"


@dataclass(frozen=True)
class Role(ValueObject[RoleEnum]):
    value: RoleEnum
