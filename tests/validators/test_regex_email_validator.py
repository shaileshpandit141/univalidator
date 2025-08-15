from pytest import mark

from univalidator.validators import RegexEmailValidator


def test_regex_email_validator_isinstance(
    email: RegexEmailValidator[str],
) -> None:
    """Test regex validator isinstance or not."""
    assert isinstance(email, RegexEmailValidator)


valid_test_data: list[tuple[str, bool]] = [
    ("user@example.com", True),
    ("user.name@example.co", True),
    ("user-name@sub.domain.net", True),
    ("u@d.io", True),
    ("test_user@my-domain.org", True),
]


@mark.parametrize("valid_email, expected", valid_test_data)
def test_valid_email_address(
    email: RegexEmailValidator[str],
    valid_email: str,
    expected: bool,
) -> None:
    """Test valid email address."""
    assert email.validate(valid_email) == expected


invalid_test_data: list[tuple[str, bool]] = [
    ("user@", False),
    ("@domain.com", False),
    ("user@domain", False),
    ("user@domain.", False),
    ("user@@example.com", False),
    ("uuser name@example.com", False),
]


@mark.parametrize("invalid_email, expected", invalid_test_data)
def test_invalid_email_address(
    email: RegexEmailValidator[str],
    invalid_email: str,
    expected: bool,
) -> None:
    """Test valid email address."""
    assert email.validate(invalid_email) == expected
