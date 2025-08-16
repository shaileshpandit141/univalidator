from abc import ABC, abstractmethod

from ._base_validator import BaseValidator


class BaseCompositeValidator[T](ABC):
    """Base composite validator abstract class"""

    def __init__(
        self,
        *,
        validators: list[BaseValidator[T]],
    ) -> None:
        """Initialize a base ecomposite validator."""
        self.validators = validators
        self.errors: list[str] = []
        super().__init__()

    @abstractmethod
    def add_validator(self, validator: BaseValidator[T]) -> None:
        """Add a new validator."""
        raise NotImplementedError

    @abstractmethod
    def validate(self, value: T) -> bool:
        """Return True if all validators pass."""
        raise NotImplementedError
