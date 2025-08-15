from univalidator.validators import RegexValidator


def test_regex_validator_isinstance(
    username_validator: RegexValidator[str],
) -> None:
    """Check regex validator instance create or not."""
    assert isinstance(username_validator, RegexValidator)
