from univalidator.validators import RegexValidator


def test_regex_validator_instance(
    regex_validator: RegexValidator[str],
) -> None:
    """Check regex validator instance create or not."""
    assert isinstance(regex_validator, RegexValidator)
