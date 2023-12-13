from typing import Optional

from argon2 import PasswordHasher
from argon2.exceptions import InvalidHashError, VerificationError, VerifyMismatchError

from src.application.user.services.password_service import (
    AbstractPasswordHasher,
    PasswordType,
)


class Argon2PasswordHasher(AbstractPasswordHasher):
    def __init__(self, ph: PasswordHasher, salt: Optional[bytes] = None) -> None:
        self._ph = ph
        self._salt = salt

    def hash(self, password: PasswordType) -> str:
        return self._ph.hash(password, salt=self._salt)

    def verify(self, hashed_password: PasswordType, plain_password: PasswordType) -> bool:
        try:
            return self._ph.verify(hashed_password, plain_password)
        except (InvalidHashError, VerificationError, VerifyMismatchError):
            return False
