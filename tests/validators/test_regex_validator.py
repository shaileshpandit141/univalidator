from pytest import mark

from univalidator.validators import RegexValidator


def test_regex_validator_isinstance(
    username: RegexValidator[str],
) -> None:
    """Test regex validator isinstance or not."""
    assert isinstance(username, RegexValidator)


test_data: list[tuple[str, bool]] = [
    # ✅ Valid cases
    ("Alice123", True),
    ("john_doe", True),
    ("Z9.test", True),
    ("Max_Power2025", True),
    ("a.b", True),
    ("Chris.underscore", True),
    ("mango", True),
    ("a1b2c3", True),
    ("A_1.b_2", True),
    ("abc_def.ghi", True),
    # ✅ Edge valid (length boundaries)
    ("Ab1", True),  # min length = 3
    ("A1234567890123456789", True),  # max length = 20
    # ❌ Invalid: starts incorrectly
    ("1stPlace", False),
    ("_hidden", False),
    (".startdot", False),
    # ❌ Invalid: too short / too long
    ("Al", False),
    ("A1", False),
    ("A12345678901234567890", False),  # 21 chars
    # ❌ Invalid: bad characters
    ("Bob@home", False),
    ("Space Man", False),
    ("user!", False),
    ("name#", False),
    # ❌ Invalid: ends with dot/underscore
    ("endswith.", False),
    ("endswith_", False),
    ("a_b_", False),
    ("test.", False),
    # ❌ Invalid: only special structure issues
    ("a..b", True),  # allowed (you didn't restrict consecutive dots)
    ("a__b", True),  # allowed
    ("a._b", True),  # allowed
    # ❌ Invalid: single-type but rule-breaking
    ("24563", False),  # starts with digit
]


@mark.parametrize("value, expected", test_data)
def test_username(
    username: RegexValidator[str],
    value: str,
    expected: bool,
) -> None:
    """Test valid username"""
    assert username.validate(value) == expected
