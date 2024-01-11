from app.domain.common.exceptions import AppException


class ApplicationException(AppException):
    @property
    def message(self) -> str:
        return "An application error occurred"
