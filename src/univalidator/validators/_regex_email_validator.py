from univalidator.abstractions import BaseValidator

from ._regex_validator import RegexValidator


class RegexEmailValidator[T: str](BaseValidator[T]):
    """Regex base email validator."""

    def __init__(
        self,
        *,
        error_message: str | None = None,
        pattern: str = r"^[\w\.-]+@[\w\.-]+\.\w+$",
    ) -> None:
        """Initialize a regex email validator."""
        self.pattern = pattern
        super().__init__(error_message=error_message)

    def validate(self, value: T) -> bool:
        """Validate email by using regex."""
        validator = RegexValidator[T](
            error_message=self.error_message,
            pattern=self.pattern,
        )
        is_valid = validator.validate(value)
        if is_valid:
            return True

        self.error = validator.error
        return False
