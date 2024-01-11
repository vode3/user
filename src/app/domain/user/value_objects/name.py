import re
from dataclasses import dataclass
from typing import Final, Literal, TypeAlias

from app.domain.common.exceptions import DomainException
from app.domain.common.value_objects import ValueObject


NAME_FORMAT_PATTERN: Final[re.Pattern[str]] = re.compile(r"^[a-zA-Z]+$")
NAME_MINIMUM_LENGTH: Final[int] = 1
NAME_MAXIMUM_LENGTH: Final[int] = 32

_NameType: TypeAlias = Literal["First", "Last"]


@dataclass(eq=False)
class WrongNameValue(ValueError, DomainException):
    _type: _NameType
    name: str


@dataclass(eq=False)
class NameEmpty(WrongNameValue):
    @property
    def message(self) -> str:
        return f"{self._type} name can't be empty."


@dataclass(eq=False)
class NameInvalidLength(WrongNameValue):
    @property
    def message(self) -> str:
        return (
            f"The provided {self._type.lower()} name '{self.name}' does not meet the required"
            f" length criteria. {self._type} names must be between {NAME_MINIMUM_LENGTH} and"
            f" {NAME_MAXIMUM_LENGTH} characters."
        )


@dataclass(eq=False)
class NameWrongFormat(WrongNameValue):
    @property
    def message(self) -> str:
        return f"The provided {self._type.lower()} name '{self.name}' contains invalid characters."


@dataclass(frozen=True)
class Name(ValueObject[str]):
    name_type: _NameType
    value: str

    def _validate(self) -> None:
        if not self.value:
            raise NameEmpty(self.name_type, self.value)
        if not NAME_MINIMUM_LENGTH <= len(self.value) < NAME_MAXIMUM_LENGTH:
            raise NameInvalidLength(self.name_type, self.value)
        if not NAME_FORMAT_PATTERN.match(self.value):
            raise NameWrongFormat(self.name_type, self.value)


@dataclass(frozen=True)
class FirstName(Name):
    name_type: _NameType = "First"


@dataclass(frozen=True)
class LastName(Name):
    name_type: _NameType = "Last"
