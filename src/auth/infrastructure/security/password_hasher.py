from typing import Optional

from argon2 import PasswordHasher
from argon2.exceptions import InvalidHashError, VerificationError, VerifyMismatchError

from auth.application.interfaces.security.password_hasher import AbstractPasswordHasher


class Argon2PasswordHasher(AbstractPasswordHasher):
    def __init__(self, ph: PasswordHasher, salt: Optional[bytes] = None) -> None:
        self._ph = ph
        self.__salt = salt

    def hash(self, password: str) -> str:
        return self._ph.hash(password, salt=self.__salt)

    def verify(self, hashed_password: str, plain_password: str) -> bool:
        try:
            return self._ph.verify(hashed_password, plain_password)
        except (InvalidHashError, VerificationError, VerifyMismatchError):
            return False
