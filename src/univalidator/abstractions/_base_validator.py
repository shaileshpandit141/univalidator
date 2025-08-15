from abc import ABC, abstractmethod


class BaseValidator[T](ABC):
    """Absctract class for email validator."""

    @abstractmethod
    def validate(self, data: T) -> bool:
        """This method use to validate email."""
        raise NotImplementedError
