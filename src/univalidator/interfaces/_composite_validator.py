from typing import Protocol

from ._validator import Validator


class CompositeValidator[T](Protocol):
    """Composite validator protocol."""

    validators: list[Validator[T]]

    def add_validator(self, validator: Validator[T]) -> None:
        """Add a new validator."""
        raise NotImplementedError

    def validate(self, value: T) -> bool:
        """Return True if all validators pass."""
        raise NotImplementedError
