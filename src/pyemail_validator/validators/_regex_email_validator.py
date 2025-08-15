from pyemail_validator.abstractions import BaseValidator

from ._regex_validator import RegexValidator


class RegexEmailValidator[T](BaseValidator[T]):
    """Regex base email validator."""

    def __init__(
        self,
        pattern: str = r"^[\w\.-]+@[\w\.-]+\.\w+$",
    ) -> None:
        """Common attributes initialization."""
        self.pattern = pattern

    def validate(self, data: T) -> bool:
        """Validate email by using regex."""
        regex_validator = RegexValidator[T](self.pattern)
        return regex_validator.validate(data)
