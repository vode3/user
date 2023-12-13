from abc import ABC, abstractmethod
from typing import Literal, TypeAlias, Union

from src.domain.user.exceptions import InvalidPasswordError
from src.domain.user.value_objects import HashedPassword, RawPassword


PasswordType: TypeAlias = Union[str, bytes]


class AbstractPasswordHasher(ABC):
    @abstractmethod
    def hash(self, password: PasswordType) -> str:
        raise NotImplementedError

    @abstractmethod
    def verify(self, hashed_password: PasswordType, plain_password: PasswordType) -> bool:
        raise NotImplementedError


class PasswordService:
    def __init__(self, password_hasher: AbstractPasswordHasher) -> None:
        self._hasher = password_hasher

    def hash_password(self, raw_password: RawPassword) -> HashedPassword:
        return HashedPassword(self._hasher.hash(raw_password.raw_value))

    def verify_password(
        self, hashed_password: HashedPassword, raw_password: RawPassword
    ) -> Literal[True]:
        is_verified = self._hasher.verify(hashed_password.raw_value, raw_password.raw_value)

        if not is_verified:
            raise InvalidPasswordError()

        return is_verified
