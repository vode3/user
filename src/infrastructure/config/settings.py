import datetime
from functools import lru_cache
from os import PathLike
from pathlib import Path
from typing import Final, Literal, Optional, TypeAlias, Union

from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


ENV_FILE: Final[str] = "./.env"


_StrPath: TypeAlias = Union[PathLike[str], str, Path]
_Algorithm: TypeAlias = Literal[
    "HS256",
    "HS384",
    "HS512",
    "RS256",
    "RS384",
    "RS512",
]


class JWTSettings(BaseSettings):
    access_secret: str
    refresh_secret: str
    algorithm: _Algorithm
    access_exp: datetime.timedelta
    refresh_exp: datetime.timedelta

    model_config = SettingsConfigDict(
        env_prefix="JWT_",
        env_file=ENV_FILE,
        env_file_encoding="utf-8",
        case_sensitive=False,
    )

    @field_validator("access_exp", mode="before")
    @classmethod
    def _validate_access_exp(cls, v: str) -> datetime.timedelta:
        return datetime.timedelta(minutes=int(v))

    @field_validator("refresh_exp", mode="before")
    @classmethod
    def _validate_refresh_exp(cls, v: str) -> datetime.timedelta:
        return datetime.timedelta(days=int(v))


class APISettings(BaseSettings):
    host: str
    port: int

    model_config = SettingsConfigDict(
        env_prefix="API_",
        env_file=ENV_FILE,
        env_file_encoding="utf-8",
        case_sensitive=False,
    )


class DBSettings(BaseSettings):
    name: str
    host: str
    port: int
    user: str
    password: str

    model_config = SettingsConfigDict(
        env_prefix="DATABASE_",
        env_file=ENV_FILE,
        env_file_encoding="utf-8",
        case_sensitive=False,
    )

    @property
    def url(self) -> str:
        return "postgresql+asyncpg://{}:{}@{}:{}/{}".format(
            self.user,
            self.password,
            self.host,
            self.port,
            self.name,
        )


class Settings(BaseSettings):
    jwt: JWTSettings = JWTSettings()  # type: ignore[call-arg]
    api: APISettings = APISettings()  # type: ignore[call-arg]
    db: DBSettings = DBSettings()  # type: ignore[call-arg]

    @staticmethod
    def root_dir() -> Path:
        return Path(__file__).resolve().parent.parent.parent.parent

    @classmethod
    def path(cls, *paths: _StrPath, root_dir: Optional[Path] = None) -> Path:
        if root_dir is None:
            root_dir = cls.root_dir()
        return Path(root_dir, *paths)


@lru_cache
def load_settings() -> Settings:
    return Settings()
