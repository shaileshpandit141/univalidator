import dns.resolver  # type: ignore

from univalidator.abstractions import BaseValidator


class MXEmailRecordValidator[T: str](BaseValidator[T]):
    """Validate email mx records"""

    def __init__(
        self,
        *,
        error_message: str | None = None,
        allowed_domains: list[str] | None = None,
    ) -> None:
        """Initialize a mc email record validator."""
        self.allowed_domains = allowed_domains
        super().__init__(error_message=error_message)

    def _has_mx_record(self, domain: str) -> bool:
        "Check email has mx record or not."
        try:
            records = dns.resolver.resolve(domain, "MX")  # type: ignore
            return len(records) > 0  # type: ignore
        except dns.resolver.NoAnswer:  # type: ignore
            self.error = f"No MX records found for domain '{domain}'."
            return False
        except dns.resolver.NXDOMAIN:  # type: ignore
            self.error = self.error_message or f"Domain '{domain}' does not exist."
            return False

    def validate(self, value: T) -> bool:
        """Validate email mx records."""
        domain = value.split("@")[-1]
        if self.allowed_domains:
            if domain in self.allowed_domains:
                return self._has_mx_record(domain)
            self.error = f"Domain {domain} is not allowed."
            return False
        return self._has_mx_record(domain)
