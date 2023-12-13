from dataclasses import dataclass
from enum import Enum

from src.domain.common.exceptions import DomainException
from src.domain.common.value_objects import ValueObject


class RoleEnum(Enum):
    ADMIN = "admin"
    USER = "user"


@dataclass(eq=False)
class WrongRoleValue(ValueError, DomainException):
    role: str


@dataclass(eq=False)
class RoleEmpty(WrongRoleValue):
    @property
    def message(self) -> str:
        return "Role can't be empty."


@dataclass(eq=False)
class RoleInvalidValue(WrongRoleValue):
    @property
    def message(self) -> str:
        return f"Invalid role: '{self.role}'."


@dataclass(frozen=True)
class Role(ValueObject[str]):
    value: str

    def _validate(self) -> None:

        if not self.value:
            raise RoleEmpty(self.value)
        try:
            RoleEnum(self.value)
        except ValueError:
            raise RoleInvalidValue(self.value)
