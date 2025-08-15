from pytest import mark

from univalidator.validators import MXEmailRecordValidator


def test_mxemail_record_validator_isinstance(
    mxemail: MXEmailRecordValidator[str],
) -> None:
    """Test mx email record validator isinstance or not."""
    assert isinstance(mxemail, MXEmailRecordValidator)


valid_test_data: list[tuple[str, bool]] = [
    ("y646896@gmail.com", True),
    ("ios646896@gmail.com", True),
    ("shaileshpandit141@gmail.com", True),
    ("shaileshpandit141@dock.com", True),
    ("@domain.com", True),
    ("user@example.com", True),
]


@mark.parametrize("valid_email, expected", valid_test_data)
def test_valid_mxemail_record(
    mxemail: MXEmailRecordValidator[str],
    valid_email: str,
    expected: bool,
) -> None:
    """Test mx email record."""
    assert mxemail.validate(valid_email) == expected


invalid_test_data: list[tuple[str, bool]] = [
    ("user@", False),
    ("user@domain", False),
    ("user@domain.", False),
    ("user@domain.c", False),
    ("eve@test-no-mx.invalid", False),
]


@mark.parametrize("invalid_email, expected", invalid_test_data)
def test_invalid_mxemail_record(
    mxemail: MXEmailRecordValidator[str],
    invalid_email: str,
    expected: bool,
) -> None:
    """Test valid email address."""
    assert mxemail.validate(invalid_email) == expected


valid_test_datax: list[tuple[str, bool]] = [
    ("y646896@gmail.com", True),
    ("ios646896@gmail.com", True),
    ("shaileshpandit141@dock.com", False),
]


@mark.parametrize("valid_email, expected", valid_test_datax)
def test_valid_mxemail_record_with_allowed_domains(
    mxemail_with_allowed_domains: MXEmailRecordValidator[str],
    valid_email: str,
    expected: bool,
) -> None:
    """Test mx email record."""
    assert mxemail_with_allowed_domains.validate(valid_email) == expected


invalid_test_datax: list[tuple[str, bool]] = [
    ("shaileshpandit141@dock.com", False),
    ("shaileshpandit141@outlook.com", False),
    ("shaileshpandit141@outlook.com", False),
]


@mark.parametrize("invalid_email, expected", invalid_test_datax)
def test_invalid_mxemail_record_with_allowed_domains(
    mxemail_with_allowed_domains: MXEmailRecordValidator[str],
    invalid_email: str,
    expected: bool,
) -> None:
    """Test valid email address."""
    assert mxemail_with_allowed_domains.validate(invalid_email) == expected
