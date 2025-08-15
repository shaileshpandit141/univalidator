from pytest import fixture

from univalidator.validators import RegexValidator


@fixture
def regex_validator() -> RegexValidator[str]:
    """Create regex validator instance and return it."""
    return RegexValidator(
        pattern=r"^[A-Za-z][A-Za-z0-9._]{2,19}$",
    )
