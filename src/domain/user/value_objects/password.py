import re
from dataclasses import dataclass
from typing import Final

from src.domain.common.exceptions import DomainException
from src.domain.common.value_objects import ValueObject


CHARS_PASSWORD_PATTERN: Final[re.Pattern[str]] = re.compile(r"[@$!%*?&]")
DIGIT_PASSWORD_PATTERN: Final[re.Pattern[str]] = re.compile(r"\d")
LOWER_PASSWORD_PATTERN: Final[re.Pattern[str]] = re.compile(r"[a-zа-я]")  # noqa: RUF001
UPPER_PASSWORD_PATTERN: Final[re.Pattern[str]] = re.compile(r"[A-ZА-Я]")  # noqa: RUF001
MIN_PASSWORD_LENGTH: Final[int] = 8
MAX_PASSWORD_LENGTH: Final[int] = 64


class WrongPasswordValue(ValueError, DomainException):
    pass


class PasswordEmpty(WrongPasswordValue):
    @property
    def message(self) -> str:
        return "Password can't be empty."


class PasswordInvalidLength(WrongPasswordValue):
    @property
    def message(self) -> str:
        return (
            "The provided password does not meet the required length criteria."
            f" Passwords must be between {MIN_PASSWORD_LENGTH} and"
            f" {MAX_PASSWORD_LENGTH} characters."
        )


class PasswordMissingSpecialChars(WrongPasswordValue):
    @property
    def message(self) -> str:
        return (
            "The provided password must contain at least one of the following special characters:"
            f" {' '.join(CHARS_PASSWORD_PATTERN.pattern[1:-1])}"
        )


class PasswordMissingDigit(WrongPasswordValue):
    @property
    def message(self) -> str:
        return "The provided password must contain at least one digit."


class PasswordMissingLowerCase(WrongPasswordValue):
    @property
    def message(self) -> str:
        return "The provided password must contain at least one lowercase letter."


class PasswordMissingUpperCase(WrongPasswordValue):
    @property
    def message(self) -> str:
        return "The provided password must contain at least one uppercase letter."


@dataclass(frozen=True)
class RawPassword(ValueObject[str]):
    value: str

    def _validate(self) -> None:
        if not self.value:
            raise PasswordEmpty()
        if not MIN_PASSWORD_LENGTH <= len(self.value) < MAX_PASSWORD_LENGTH:
            raise PasswordInvalidLength()
        if not CHARS_PASSWORD_PATTERN.search(self.value):
            raise PasswordMissingSpecialChars()
        if not DIGIT_PASSWORD_PATTERN.search(self.value):
            raise PasswordMissingDigit()
        if not LOWER_PASSWORD_PATTERN.search(self.value):
            raise PasswordMissingLowerCase()
        if not UPPER_PASSWORD_PATTERN.search(self.value):
            raise PasswordMissingUpperCase()


@dataclass(frozen=True)
class HashedPassword(ValueObject[str]):
    value: str
