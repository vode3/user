from abc import ABC, abstractmethod
from typing import Any, MutableMapping, TypeAlias


Payload: TypeAlias = MutableMapping[str, Any]


class AbstractTokenGenerator(ABC):
    @abstractmethod
    def decode(self, token: str, secret_key: str) -> Payload:
        raise NotImplementedError

    @abstractmethod
    def encode(self, payload: Payload, secret_key: str) -> str:
        raise NotImplementedError
