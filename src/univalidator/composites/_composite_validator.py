from univalidator.abstractions import BaseCompositeValidator, BaseValidator


class CompositeValidator[T](BaseCompositeValidator[T]):
    """Runs multiple validators on given data."""

    def add_validator(self, validator: BaseValidator[T]) -> None:
        """Add a new validator."""
        self.validators.append(validator)

    def validate(self, value: T) -> bool:
        """Return True if all validators pass."""
        is_valid: list[bool] = []
        errors: list[str] = []

        for validator in self.validators:
            if validator.validate(value):
                is_valid.append(True)
            else:
                is_valid.append(False)
                errors.append(validator.error)

        self.errors = errors
        return all(is_valid)
