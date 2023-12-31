from abc import ABC, abstractmethod
from types import TracebackType
from typing import Generic, Optional, Self, Type, TypeVar


SessionType = TypeVar("SessionType")
TransactionType = TypeVar("TransactionType")


class UnitOfWork(ABC, Generic[SessionType, TransactionType]):
    def __init__(self, session: SessionType) -> None:
        self._session = session
        self._transaction: Optional[TransactionType] = None

    async def __aenter__(self) -> Self:
        await self._create_transaction()
        return self

    async def __aexit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_value: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> None:

        if self._transaction:
            if exc_type:
                await self.rollback()
            else:
                await self.commit()

        await self._close_transaction()

    @abstractmethod
    async def commit(self) -> None:
        raise NotImplementedError

    @abstractmethod
    async def rollback(self) -> None:
        raise NotImplementedError

    @abstractmethod
    async def _create_transaction(self) -> None:
        raise NotImplementedError

    @abstractmethod
    async def _close_transaction(self) -> None:
        raise NotImplementedError
