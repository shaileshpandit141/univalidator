from re import Match, match

from univalidator.abstractions import BaseValidator


class RegexValidator[T: str](BaseValidator[T]):
    """Regex base email validator."""

    def __init__(
        self,
        *,
        error_message: str | None = None,
        pattern: str,
    ) -> None:
        """Initialize a regex validator."""
        self.pattern = pattern
        super().__init__(error_message=error_message)

    def validate(self, value: T) -> bool:
        """Validate data by using regex."""
        matched: Match[str] | None = match(self.pattern, value)
        if matched is not None:
            return True

        self.error = self.error_message or "Value does not match the required format."
        return False
