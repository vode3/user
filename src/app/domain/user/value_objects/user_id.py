from dataclasses import dataclass
from uuid import UUID

from app.domain.common.value_objects import ValueObject


@dataclass(frozen=True)
class UserId(ValueObject[UUID]):
    value: UUID
