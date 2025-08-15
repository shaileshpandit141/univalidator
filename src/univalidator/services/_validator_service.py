from univalidator.abstractions import BaseValidator


class ValidatorService[T]:
    """Runs multiple validators on given data."""

    def __init__(self, validators: list[BaseValidator[T]]) -> None:
        """Initialize validators attributes."""
        self.validators = validators

    def add_validator(self, validator: BaseValidator[T]) -> None:
        """Add a new validator."""
        self.validators.append(validator)

    def validate(self, data: T) -> bool:
        """Return True if all validators pass."""
        return all(validator.validate(data) for validator in self.validators)
