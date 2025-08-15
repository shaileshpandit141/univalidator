from pytest import mark

from univalidator.validators import RegexEmailValidator


def test_regex_email_validator_isinstance(
    email: RegexEmailValidator[str],
) -> None:
    """Test regex validator isinstance or not."""
    assert isinstance(email, RegexEmailValidator)
