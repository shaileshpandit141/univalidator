from univalidator.validators import RegexValidator


def test_regex_validator_isinstance(
    username: RegexValidator[str],
) -> None:
    """Test regex validator isinstance or not."""
    assert isinstance(username, RegexValidator)


def test_valid_username(
    username: RegexValidator[str],
) -> None:
    """Test valid username"""
    assert username.validate("username1")
    assert username.validate("username1.2")
    assert username.validate("user_name2")


def test_invalid_username(
    username: RegexValidator[str],
) -> None:
    """Test invalid username"""
    assert not username.validate("25user")
    assert not username.validate(".user")
    assert not username.validate("@user")
