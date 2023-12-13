from abc import ABC
from dataclasses import dataclass
from typing import Any, Generic, TypeVar, cast

from src.domain.common.exceptions import DomainException


T = TypeVar("T", bound=Any)


@dataclass(eq=False)
class WrongValue(Generic[T], ValueError, DomainException):
    value: T
    expected_type: str

    @property
    def message(self) -> str:
        return f"The provided value '{self.value}' must be of type '{self.expected_type}'."


@dataclass(frozen=True, eq=True)
class ValueObject(ABC, Generic[T]):
    value: T

    def __post_init__(self) -> None:
        self._check_type()
        self._validate()

    def _check_type(self) -> None:
        _type = self.__orig_bases__[0].__args__[0]  # type: ignore[attr-defined]
        if not isinstance(self.value, _type):
            raise WrongValue(self.value, cast(str, _type.__name__))

    def _validate(self) -> None:
        pass

    @property
    def raw_value(self) -> T:
        return self.value
