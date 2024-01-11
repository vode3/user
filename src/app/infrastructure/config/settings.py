from functools import lru_cache
from os import PathLike
from pathlib import Path
from typing import Final, Optional, TypeAlias, Union

from pydantic_settings import BaseSettings, SettingsConfigDict


ENV_FILE: Final[str] = "./.env"


_StrPath: TypeAlias = Union[PathLike[str], str, Path]


class APISettings(BaseSettings):
    host: str
    port: int

    model_config = SettingsConfigDict(
        env_prefix="APP_",
        env_file=ENV_FILE,
        env_file_encoding="utf-8",
        case_sensitive=False,
    )


class AuthSettings(BaseSettings):
    host: str
    port: int

    model_config = SettingsConfigDict(
        env_prefix="AUTH_",
        env_file=ENV_FILE,
        env_file_encoding="utf-8",
        case_sensitive=False,
    )


class DatabaseSettings(BaseSettings):
    uri: str
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
        if "sqlite" in self.uri:
            return self.uri.format(self.name)
        return self.uri.format(
            self.user,
            self.password,
            self.host,
            self.port,
            self.name,
        )


class Settings(BaseSettings):
    api: APISettings = APISettings()  # type: ignore[call-arg]
    auth: AuthSettings = AuthSettings()  # type: ignore[call-arg]
    db: DatabaseSettings = DatabaseSettings()  # type: ignore[call-arg]

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
