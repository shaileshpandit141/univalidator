from abc import ABC, abstractmethod


class BaseValidator(ABC):
    """Absctract class for email validator."""

    @abstractmethod
    def validate(self, email: str) -> bool:
        """This method use to validate email."""
        raise NotImplementedError
