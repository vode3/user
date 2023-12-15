from abc import ABC
from dataclasses import dataclass
from typing import Any, Generic, TypeVar


EntityId = TypeVar("EntityId")


@dataclass
class Entity(ABC, Generic[EntityId]):
    id: EntityId

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, self.__class__) and self.id == other.id

    def __hash__(self) -> int:
        return hash(self.id)

    def to_dict(self) -> dict[str, Any]:
        return {k: v for k, v in self.__dict__.items() if not k.startswith("_")}


@dataclass(kw_only=True)
class AggregateRoot(Entity[EntityId], ABC): ...
