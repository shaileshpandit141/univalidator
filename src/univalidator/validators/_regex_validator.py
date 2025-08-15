from re import match

from univalidator.abstractions import BaseValidator


class RegexValidator[T](BaseValidator[T]):
    """Regex base email validator."""

    def __init__(
        self,
        pattern: str,
    ) -> None:
        """Common attributes initialization."""
        self.pattern = pattern

    def validate(self, data: T) -> bool:
        """Validate data by using regex."""
        if isinstance(data, str):
            return match(self.pattern, data) is not None
        return False
