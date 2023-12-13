from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from src.application.common.dto.base import DTO


@dataclass(frozen=True)
class UserDTO(DTO):
    id: UUID
    first_name: str
    last_name: str
    username: str
    email: str


@dataclass(frozen=True)
class DeletedUserDTO(DTO):
    id: UUID
    first_name: str
    last_name: str
    username: str
    email: str
    deleted_at: datetime
