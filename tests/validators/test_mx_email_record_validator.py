from pytest import mark

from univalidator.validators import MXEmailRecordValidator


def test_mxemail_record_validator_isinstance(
    mxemail: MXEmailRecordValidator[str],
) -> None:
    """Test mx email record validator isinstance or not."""
    assert isinstance(mxemail, MXEmailRecordValidator)


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
def test_valid_mxemail_record(
    mxemail: MXEmailRecordValidator[str],
    value: str,
    expected: bool,
) -> None:
    """Test mx email record."""
    assert mxemail.validate(value) == expected


test_data_allowed_domains: list[tuple[str, bool]] = [
    ("y646896@gmail.com", True),
    ("ios646896@gmail.com", True),
    ("shaileshpandit141@dock.com", False),
    ("shaileshpandit141@dock.com", False),
    ("shaileshpandit141@outlook.com", False),
    ("shaileshpandit141@outlook.com", False),
]


@mark.parametrize("value, expected", test_data_allowed_domains)
def test_valid_mxemail_record_with_allowed_domains(
    mxemail_with_allowed_domains: MXEmailRecordValidator[str],
    value: str,
    expected: bool,
) -> None:
    """Test mx email record."""
    assert mxemail_with_allowed_domains.validate(value) == expected
