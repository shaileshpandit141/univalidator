from pyemail_validator.abstractions import BaseValidator


class ValidatorService[T]:
    """Validate data base on validator"""

    def __init__(self, validators: list[BaseValidator[T]]) -> None:
        """Initialize all validators attributes"""
        self.validators = validators

    def add_validator(self, validator: BaseValidator[T]) -> None:
        """Add new validator"""
        self.validators.append(validator)

    def validate(self, data: T) -> bool:
        for validator in self.validators:
            if not validator.validate(data):
                return False
        return True
