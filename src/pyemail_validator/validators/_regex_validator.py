from re import match

from pyemail_validator.abstractions import BaseValidator


class RegexValidator(BaseValidator):
    """Regex base email validator."""

    def __init__(
        self,
        pattern: str = r"^[\w\.-]+@[\w\.-]+\.\w+$",
    ) -> None:
        """Common attributes initialization."""
        self.pattern = pattern

    def validate(self, email: str) -> bool:
        """Validate email by using regex."""
        return match(self.pattern, email) is not None
