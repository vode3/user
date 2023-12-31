from sqlalchemy import Enum, String
from sqlalchemy.orm import Mapped, mapped_column

from src.domain.user.value_objects.role import RoleEnum
from src.infrastructure.db.models.base import Base
from src.infrastructure.db.models.base.mixins import TimeMixin, UUIDMixin


class User(Base, UUIDMixin, TimeMixin):
    first_name: Mapped[str] = mapped_column(String)
    last_name: Mapped[str] = mapped_column(String)
    username: Mapped[str] = mapped_column(String, unique=True, index=True)
    email: Mapped[str] = mapped_column(String, unique=True, index=True)
    password: Mapped[str] = mapped_column(String)
    role: Mapped[RoleEnum] = mapped_column(Enum(RoleEnum, name="role_enum"))
