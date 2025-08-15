from pytest import mark

from univalidator.composites import CompositeValidator


def test_composite_validator_isinstance(
    composite_email: CompositeValidator[str],
) -> None:
    """Test composite validator isinstance or not."""
    assert isinstance(composite_email, CompositeValidator)


test_data: list[tuple[str, bool]] = [
    ("y646896@gmail.com", True),
    ("ios646896@gmail.com", True),
    ("shaileshpandit141@gmail.com", True),
    ("shaileshpandit141@dock.com", True),
    ("user@example.com", True),
    ("user@", False),
    ("user@domain", False),
    ("user@domain.", False),
    ("user@domain.c", False),
]


@mark.parametrize("value, expected", test_data)
def test_composite_email_address(
    composite_email: CompositeValidator[str],
    value: str,
    expected: bool,
) -> None:
    """Test valid email address."""
    assert composite_email.validate(value) == expected
