from pytest import fixture

from univalidator.composites import CompositeValidator
from univalidator.validators import (
    EmailMxValidator,
    RegexEmailValidator,
    RegexValidator,
)


@fixture
def username() -> RegexValidator[str]:
    """Create regex validator instance and return it."""
    return RegexValidator(r"^[A-Za-z][A-Za-z0-9._]{1,18}[A-Za-z0-9]$")


@fixture
def email() -> RegexEmailValidator[str]:
    """Create regex email validator instance and return it."""
    return RegexEmailValidator[str]()


@fixture
def email_mx() -> EmailMxValidator[str]:
    """Create mx email record validator instance and return it."""
    return EmailMxValidator[str]()


@fixture
def email_mx_with_allowed_domains() -> EmailMxValidator[str]:
    """Create mx email record validator instance and return it."""
    return EmailMxValidator[str](
        allowed_domains=["gmail.com"],
    )


@fixture
def composite_email() -> CompositeValidator[str]:
    "Run multiple validators."
    return CompositeValidator[str](
        validators=[
            RegexEmailValidator[str](),
            EmailMxValidator[str](),
        ]
    )
