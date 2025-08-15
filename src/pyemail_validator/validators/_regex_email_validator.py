from pyemail_validator.abstractions import BaseValidator

from ._regex_validator import RegexValidator


class RegexEmailValidator(BaseValidator):
    """Regex base email validator."""

    def __init__(
        self,
        pattern: str = r"^[\w\.-]+@[\w\.-]+\.\w+$",
    ) -> None:
        """Common attributes initialization."""
        self.pattern = pattern

    def validate(self, email: str) -> bool:
        """Validate email by using regex."""
        regex_validator = RegexValidator(self.pattern)
        return regex_validator.validate(email)
