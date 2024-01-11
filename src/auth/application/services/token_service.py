from datetime import datetime, timedelta
from uuid import UUID

from auth.application.interfaces.security.token_generator import (
    AbstractTokenGenerator,
    Payload,
)


class TokenService:
    def __init__(
        self,
        token_generator: AbstractTokenGenerator,
        access_secret: str,
        refresh_secret: str,
        access_expire_time: timedelta,
        refresh_expire_time: timedelta,
    ) -> None:
        self._generator = token_generator
        self._access_secret = access_secret
        self._refresh_secret = refresh_secret
        self._access_expire_time = access_expire_time
        self._refresh_expire_time = refresh_expire_time

    def create_access_token(self, user_id: UUID) -> str:
        return self._create_token(user_id, self._access_expire_time, self._access_secret)

    def create_refresh_token(self, user_id: UUID) -> str:
        return self._create_token(user_id, self._refresh_expire_time, self._refresh_secret)

    def validate_access_token(self, token: str) -> Payload:
        return self._validate_token(token, self._access_secret)

    def validate_refresh_token(self, token: str) -> Payload:
        return self._validate_token(token, self._refresh_secret)

    def _create_token(self, user_id: UUID, expire_time: timedelta, secret_key: str) -> str:
        iat = datetime.utcnow()
        exp = iat + expire_time
        sub = str(user_id)

        payload = {"sub": sub, "iat": iat, "exp": exp}

        return self._generator.encode(payload=payload, secret_key=secret_key)

    def _validate_token(self, token: str, secret_key: str) -> Payload:
        payload = self._generator.decode(token, secret_key)

        if not payload:
            raise Exception("Invalid token")  # TODO Create custom exception  # noqa: FIX002

        return payload
