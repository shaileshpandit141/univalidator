from univalidator.composites import CompositeValidator


def test_composite_validator_isinstance(
    composite_email: CompositeValidator[str],
) -> None:
    """Test composite validator isinstance or not."""
    assert isinstance(composite_email, CompositeValidator)
