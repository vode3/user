class AppException(Exception):
    def __str__(self) -> str:
        return self.message

    @property
    def message(self) -> str:
        return "An app error occurred"


class DomainException(AppException):
    @property
    def message(self) -> str:
        return "A domain error occurred"
