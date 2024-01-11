from jose import jwt
from jose.exceptions import ExpiredSignatureError, JWTClaimsError, JWTError

from auth.application.interfaces.security.token_generator import (
    AbstractTokenGenerator,
    Payload,
)


class JwtTokenGenerator(AbstractTokenGenerator):
    def __init__(self, algorithm: str) -> None:
        self._algorithm = algorithm

    def decode(self, token: str, secret_key: str) -> Payload:
        try:
            payload = jwt.decode(token, secret_key, algorithms=[self._algorithm])
        except (ExpiredSignatureError, JWTClaimsError, JWTError):
            payload = {}
        return payload

    def encode(self, payload: Payload, secret_key: str) -> str:
        return jwt.encode(payload, secret_key, algorithm=self._algorithm)
