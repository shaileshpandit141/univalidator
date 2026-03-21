from typing import Never

import dns.resolver  # type: ignore

from univalidator.interfaces import Validator


class EmailMxValidator[T: str](Validator[T]):
    """Validate email mx records"""

    def __init__(self, allowed_domains: list[str] | None = None) -> None:
        """Initialize a mc email record attrs."""
        self.allowed_domains = allowed_domains

    def raise_error(self, message: str) -> Never:
        raise ValueError(message)

    def _has_mx_record(self, domain: str, raise_on_error: bool) -> bool:
        "Check email has mx record or not."
        try:
            records = dns.resolver.resolve(domain, "MX")  # type: ignore
            return len(records) > 0
        except dns.resolver.NoAnswer:
            if raise_on_error:
                raise self.raise_error(f"No MX records found for domain '{domain}'.")
        except dns.resolver.NXDOMAIN:
            if raise_on_error:
                raise self.raise_error(f"Domain '{domain}' does not exist.")
        except dns.resolver.Timeout:
            if raise_on_error:
                raise self.raise_error(f"DNS lookup for '{domain}' timed out.")
        except dns.resolver.NoNameservers:
            if raise_on_error:
                raise self.raise_error(f"No nameservers available for '{domain}'.")
        return False

    def validate(self, value: T, raise_on_error: bool = False) -> bool:
        """Validate email mx records."""
        return self._has_mx_record(
            value.split("@")[-1],
            raise_on_error,
        )
