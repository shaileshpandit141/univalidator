from univalidator.validators import RegexValidator


def test_regex_validator_isinstance(
    username_validator: RegexValidator[str],
) -> None:
    """Test regex validator isinstance or not."""
    assert isinstance(username_validator, RegexValidator)


def test_valid_username(
    username_validator: RegexValidator[str],
) -> None:
    """Test valid username"""
    assert username_validator.validate("username1")
    assert username_validator.validate("username1.2")
    assert username_validator.validate("user_name2")
