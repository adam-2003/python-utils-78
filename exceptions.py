class CustomError(Exception):
    """Base class for custom exceptions."""
    pass

class ValidationError(CustomError):
    """Exception raised for validation errors."""

    def __init__(self, message: str, field: str) -> None:
        super().__init__(message)
        self.field = field
        self.message = message

    def __str__(self) -> str:
        return f'ValidationError for {self.field}: {self.message}'

class NotFoundError(CustomError):
    """Exception raised when a resource is not found."""

    def __init__(self, resource: str) -> None:
        super().__init__(f'{resource} not found')
        self.resource = resource

    def __str__(self) -> str:
        return f'NotFoundError: {self.resource} not found'