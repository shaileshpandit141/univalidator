from abc import ABC, abstractmethod


class BaseValidator[T](ABC):
    """Absctract class for email validator."""

    def __init__(
        self,
        *,
        error_message: str | None = None,
    ) -> None:
        """Initialize a base validator."""
        self.error_message = error_message or ""
        self.error: str = ""
        super().__init__()

    @abstractmethod
    def validate(self, value: T) -> bool:
        """This method use to validate email."""
        raise NotImplementedError
