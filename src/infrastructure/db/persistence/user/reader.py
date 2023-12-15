from src.domain.user.interfaces.persistence.reader import UserReader
from src.infrastructure.db.persistence.base import SQLAlchemyGateway


class SQLAlchemyUserReader(SQLAlchemyGateway, UserReader): ...
