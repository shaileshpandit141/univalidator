from pytest import mark

from univalidator.validators import EmailMxValidator


def test_email_mx_validator_isinstance(
    email_mx: EmailMxValidator[str],
) -> None:
    """Test mx email record validator isinstance or not."""
    assert isinstance(email_mx, EmailMxValidator)


test_data: list[tuple[str, bool]] = [
    ("y646896@gmail.com", True),
    ("ios646896@gmail.com", True),
    ("shaileshpandit141@gmail.com", True),
    ("shaileshpandit141@dock.com", True),
    ("@domain.com", True),
    ("user@example.com", True),
    ("user@", False),
    ("user@domain", False),
    ("user@domain.", False),
    ("user@domain.c", False),
    ("eve@test-no-mx.invalid", False),
]


@mark.parametrize("value, expected", test_data)
def test_email_mx_record(
    email_mx: EmailMxValidator[str],
    value: str,
    expected: bool,
) -> None:
    """Test mx email record."""
    assert email_mx.validate(value) == expected


test_data_allowed_domains: list[tuple[str, bool]] = [
    ("y646896@gmail.com", True),
    ("ios646896@gmail.com", True),
    ("shaileshpandit141@outlook.com", True),
    ("shaileshpandit141@xyz.com", True),
]


@mark.parametrize("value, expected", test_data_allowed_domains)
def test_email_mx_with_allowed_domains(
    email_mx_with_allowed_domains: EmailMxValidator[str],
    value: str,
    expected: bool,
) -> None:
    """Test mx email record."""
    assert email_mx_with_allowed_domains.validate(value) == expected
