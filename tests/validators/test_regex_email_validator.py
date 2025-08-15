from pytest import mark

from univalidator.validators import RegexEmailValidator


def test_regex_email_validator_isinstance(
    email: RegexEmailValidator[str],
) -> None:
    """Test regex validator isinstance or not."""
    assert isinstance(email, RegexEmailValidator)


test_data: list[tuple[str, bool]] = [
    ("user@example.com", True),
    ("user.name@example.co", True),
    ("user-name@sub.domain.net", True),
    ("u@d.io", True),
    ("test_user@my-domain.org", True),
    ("user@", False),
    ("@domain.com", False),
    ("user@domain", False),
    ("user@domain.", False),
    ("user@@example.com", False),
    ("uuser name@example.com", False),
]


@mark.parametrize("value, expected", test_data)
def test_valid_email_address(
    email: RegexEmailValidator[str],
    value: str,
    expected: bool,
) -> None:
    """Test valid email address."""
    assert email.validate(value) == expected
