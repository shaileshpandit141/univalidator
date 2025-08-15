from pytest import mark

from univalidator.validators import RegexValidator


def test_regex_validator_isinstance(
    username: RegexValidator[str],
) -> None:
    """Test regex validator isinstance or not."""
    assert isinstance(username, RegexValidator)


test_data: list[tuple[str, bool]] = [
    ("Alice123", True),
    ("john_doe", True),
    ("Z9.test", True),
    ("Max_Power2025", True),
    ("a.b", True),
    ("Chris.underscore", True),
    ("s2.", True),
    ("1stPlace", False),
    ("_hidden", False),
    ("Al", False),
    ("Bob@home", False),
    ("toolooooooooooooooooong", False),
    ("24563", False),
    ("Space Man", False),
]


@mark.parametrize("value, expected", test_data)
def test_valid_username(
    username: RegexValidator[str],
    value: str,
    expected: bool,
) -> None:
    """Test valid username"""
    assert username.validate(value) == expected
