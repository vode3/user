from src.domain.user.entities import User
from src.infrastructure.db.models.base import mapper_registry, metadata
from src.infrastructure.db.models.user import user_table


__all__ = (
    "metadata",
    "user_table",
)

mapper_registry.map_imperatively(User, user_table)
