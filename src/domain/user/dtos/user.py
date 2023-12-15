from dataclasses import dataclass
from uuid import UUID

from src.application.common.dtos import DTO


@dataclass(frozen=True)
class UserDTO(DTO):
    id: UUID
    first_name: str
    last_name: str
    username: str
    email: str
