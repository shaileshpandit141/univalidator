from typing import Protocol


class Validator[T](Protocol):
    """Validator protocol."""

    def validate(self, value: T) -> bool:
        raise NotImplementedError
