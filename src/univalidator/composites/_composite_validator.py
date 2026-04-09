from univalidator.interfaces import Validator


class CompositeValidator[T]:
    """Runs multiple validators on given data."""

    def __init__(self, validators: list[Validator[T]]) -> None:
        self.validators = validators

    def add_validator(self, validator: Validator[T]) -> None:
        """Add a new validator."""
        self.validators.append(validator)

    def validate(self, value: T) -> bool:
        """Return True if all validators pass."""

        for validator in self.validators:
            if validator.validate(value):
                continue
            else:
                return False

        return True
