import re
from dataclasses import dataclass
from typing import Final

from app.domain.common.exceptions import DomainException
from app.domain.common.value_objects import ValueObject


USERNAME_FORMAT_PATTERN: Final[re.Pattern[str]] = re.compile(r"^[a-zA-Z0-9-_]+$")
USERNAME_MINIMUM_LENGTH: Final[int] = 5
USERNAME_MAXIMUM_LENGTH: Final[int] = 20


@dataclass(eq=False)
class WrongUsernameValue(ValueError, DomainException):
    username: str


@dataclass(eq=False)
class UsernameEmpty(WrongUsernameValue):
    @property
    def message(self) -> str:
        return "Username can't be empty."


@dataclass(eq=False)
class UsernameInvalidLength(WrongUsernameValue):
    @property
    def message(self) -> str:
        return (
            f"The provided username '{self.username}' does not meet the required length criteria."
            f" Usernames must be between {USERNAME_MINIMUM_LENGTH} and"
            f" {USERNAME_MAXIMUM_LENGTH} characters."
        )


@dataclass(eq=False)
class UsernameWrongFormat(WrongUsernameValue):
    @property
    def message(self) -> str:
        return f"The provided username '{self.username}' contains invalid characters."


@dataclass(frozen=True)
class Username(ValueObject[str]):
    value: str

    def _validate(self) -> None:
        if not self.value:
            raise UsernameEmpty(self.value)
        if not USERNAME_MINIMUM_LENGTH <= len(self.value) < USERNAME_MAXIMUM_LENGTH:
            raise UsernameInvalidLength(self.value)
        if not USERNAME_FORMAT_PATTERN.match(self.value):
            raise UsernameWrongFormat(self.value)
