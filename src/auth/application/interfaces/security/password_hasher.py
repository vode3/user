from abc import ABC, abstractmethod


class AbstractPasswordHasher(ABC):
    @abstractmethod
    def hash(self, password: str) -> str:
        raise NotImplementedError

    @abstractmethod
    def verify(self, hashed_password: str, plain_password: str) -> bool:
        raise NotImplementedError
