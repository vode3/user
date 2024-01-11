from typing import Literal

from auth.application.interfaces.security.password_hasher import AbstractPasswordHasher


class PasswordService:
    def __init__(self, password_hasher: AbstractPasswordHasher) -> None:
        self._hasher = password_hasher

    def hash_password(self, raw_password: str) -> str:
        return self._hasher.hash(raw_password)

    def verify_password(self, hashed_password: str, raw_password: str) -> Literal[True]:
        is_verified = self._hasher.verify(hashed_password, raw_password)

        if not is_verified:
            raise Exception("Invalid password")  # TODO Create custom exception  # noqa: FIX002

        return is_verified
