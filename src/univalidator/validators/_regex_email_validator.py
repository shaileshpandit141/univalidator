from univalidator.interfaces import Validator

from ._regex_validator import RegexValidator


class RegexEmailValidator[T: str](Validator[T]):
    """Regex base email validator."""

    def __init__(self, pattern: str = r"^[\w\.-]+@[\w\.-]+\.\w+$") -> None:
        """Initialize a regex email validator."""
        self.pattern = pattern

    def validate(self, value: T) -> bool:
        """Validate email by using regex."""
        validator = RegexValidator[T](self.pattern)
        return validator.validate(value)
