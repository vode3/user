import re
from dataclasses import dataclass
from typing import Final

from src.domain.common.exceptions import DomainException
from src.domain.common.value_objects import ValueObject


EMAIL_FORMAT_PATTERN: Final[re.Pattern[str]] = re.compile(
    r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
)


@dataclass(eq=False)
class WrongEmailValue(ValueError, DomainException):
    email: str


@dataclass(eq=False)
class EmailEmpty(WrongEmailValue):
    @property
    def message(self) -> str:
        return "Email can't be empty."


@dataclass(eq=False)
class EmailWrongFormat(WrongEmailValue):
    @property
    def message(self) -> str:
        return f"The provided email '{self.email}' does not meet the required format condition."


@dataclass(frozen=True)
class Email(ValueObject[str]):
    value: str

    def _validate(self) -> None:
        if not self.value:
            raise EmailEmpty(self.value)
        if not EMAIL_FORMAT_PATTERN.match(self.value):
            raise EmailWrongFormat(self.value)
