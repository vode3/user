from dataclasses import dataclass

from app.domain.common.exceptions import DomainException
from app.domain.user.value_objects import UserId


@dataclass(eq=False)
class UserIsDeleted(DomainException):
    user_id: UserId

    @property
    def message(self) -> str:
        return f"The user '{self.user_id.raw_value}' is deleted."


@dataclass(eq=False)
class InvalidPasswordError(DomainException):
    @property
    def message(self) -> str:
        return "The password is invalid."


@dataclass(eq=False)
class InvalidTokenError(DomainException):
    token: str

    @property
    def message(self) -> str:
        return f"The token '{self.token}' is invalid."
