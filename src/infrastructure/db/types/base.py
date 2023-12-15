from typing import Any, Optional, Type, TypeVar

from sqlalchemy.engine import Dialect
from sqlalchemy.types import TypeDecorator, TypeEngine

from src.domain.common.value_objects.base import ValueObject


VT = TypeVar("VT")


class BaseType(TypeDecorator[ValueObject[VT]]):
    impl: TypeEngine[Any] | Type[TypeEngine[Any]]
    _vo: Type[ValueObject[VT]]

    def process_bind_param(
        self, value: Optional[ValueObject[VT]], dialect: Dialect
    ) -> Optional[VT]:
        if value is None:
            return value
        return value.raw_value

    def process_result_value(
        self, value: Optional[VT], dialect: Dialect
    ) -> Optional[ValueObject[VT]]:
        if value is None:
            return value
        return self._vo(value)
