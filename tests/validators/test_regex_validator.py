from pytest import mark

from univalidator.validators import RegexValidator


def test_regex_validator_isinstance(
    username: RegexValidator[str],
) -> None:
    """Test regex validator isinstance or not."""
    assert isinstance(username, RegexValidator)


valid_test_data: list[tuple[str, bool]] = [
    ("Alice123", True),
    ("john_doe", True),
    ("Z9.test", True),
    ("Max_Power2025", True),
    ("a.b", True),
    ("Chris.underscore", True),
    ("s2.", True),
]


@mark.parametrize("valid_username, expected", valid_test_data)
def test_valid_username(
    username: RegexValidator[str],
    valid_username: str,
    expected: bool,
) -> None:
    """Test valid username"""
    assert username.validate(valid_username) == expected


invalid_test_data: list[tuple[str, bool]] = [
    ("1stPlace", True),
    ("_hidden", True),
    ("Al", True),
    ("Bob@home", True),
    ("toolooooooooooooooooong", True),
    ("24563", True),
    ("Space Man", True),
]


@mark.parametrize("invalid_username, expected", valid_test_data)
def test_invalid_username(
    username: RegexValidator[str],
    invalid_username: str,
    expected: bool,
) -> None:
    """Test invalid username"""
    assert username.validate(invalid_username) == expected
