import dns.resolver  # type: ignore

from univalidator.abstractions import BaseValidator


class MXEmailRecordValidator[T](BaseValidator[T]):
    """Validate email mx records"""

    def __init__(
        self,
        allowed_domains: list[str] | None = None,
    ) -> None:
        """Common attributes initialization."""
        self.allowed_domains = allowed_domains

    def _has_mx_record(self, domain: str) -> bool:
        "Check email has mx record or not."
        try:
            records = dns.resolver.resolve(domain, "MX")  # type: ignore
            return len(records) > 0  # type: ignore
        except dns.resolver.NoAnswer:  # type: ignore
            return False
        except dns.resolver.NXDOMAIN:  # type: ignore
            return False

    def validate(self, data: T) -> bool:
        """Validate email mx records."""
        if isinstance(data, str):
            domain = data.split("@")[-1]
            if self.allowed_domains:
                if domain in self.allowed_domains:
                    return self._has_mx_record(domain)
                else:
                    return False
            else:
                return self._has_mx_record(domain)
        return False
