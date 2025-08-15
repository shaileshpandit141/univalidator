from pytest import fixture

from univalidator.validators import (
    MXEmailRecordValidator,
    RegexEmailValidator,
    RegexValidator,
)


@fixture
def username() -> RegexValidator[str]:
    """Create regex validator instance and return it."""
    return RegexValidator(
        pattern=r"^[A-Za-z][A-Za-z0-9._]{2,19}$",
    )


@fixture
def email() -> RegexEmailValidator[str]:
    """Create regex email validator instance and return it."""
    return RegexEmailValidator[str]()


@fixture
def mxemail() -> MXEmailRecordValidator[str]:
    """Create mx email record validator instance and return it."""
    return MXEmailRecordValidator[str]()


@fixture
def mxemail_with_allowed_domains() -> MXEmailRecordValidator[str]:
    """Create mx email record validator instance and return it."""
    return MXEmailRecordValidator[str](["gmail.com"])
