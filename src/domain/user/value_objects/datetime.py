from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from src.domain.common.value_objects import ValueObject


@dataclass(frozen=True)
class DateTime(ValueObject[datetime]):
    value: datetime


@dataclass(frozen=True)
class CreatedAt(DateTime):
    pass


@dataclass(frozen=True)
class UpdatedAt(DateTime):
    pass


@dataclass(frozen=True)
class DeletedAt(ValueObject[Optional[datetime]]):
    pass
