from re import Match, match

from univalidator.interfaces import Validator


class RegexValidator[T: str](Validator[T]):
    """Regex base email validator."""

    def __init__(self, pattern: str) -> None:
        """Initialize a regex pattern."""
        self.pattern = pattern

    def validate(self, value: T) -> bool:
        """Validate data by using regex."""
        matched: Match[str] | None = match(self.pattern, value)
        if matched is not None:
            return True

        return False
