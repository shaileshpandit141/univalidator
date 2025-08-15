# 🛡️ univalidator

[![PyPI version](https://img.shields.io/pypi/v/univalidator.svg)](https://pypi.org/project/univalidator/)
[![Python versions](https://img.shields.io/pypi/pyversions/univalidator.svg)](https://pypi.org/project/univalidator/)
[![License](https://img.shields.io/pypi/l/univalidator.svg)](https://github.com/shaileshpandit141/univalidator/blob/main/LICENSE)

A **flexible, extensible, and type-safe** Python validation framework designed to validate data with ease.  
Currently supports **email validation** (via regex and MX records) and **composite validators** for running multiple checks.

## ✨ Features

- **Abstract Validator Interface** — define your own validators easily.
- **Regex-based Validation** — for any string patterns.
- **Email Format Validation** — RFC-compliant pattern check.
- **MX Record Validation** — verifies if an email domain can receive emails.
- **Composite Validation** — run multiple validators in sequence.
- **Type Safe** — written with modern Python type hints.

## 📦 Installation

- **By using uv:**
  
    ```bash
    uv add univalidator
    ````

- **By using pip:**

    ```bash
    pip install univalidator
    ````

## 📚 API Reference

### **1️ BaseValidator[T]**

Abstract base for all validators.
**Custom validators** must implement the `validate(data: T) -> bool` method.

### **2️ RegexValidator[T]**

Validates data against a regular expression.

```python
from univalidator.validators import RegexValidator

validator = RegexValidator[str](r"^\d{4}-\d{2}-\d{2}$")  # YYYY-MM-DD format
validator.validate("2025-08-15")  # True
validator.validate("15-08-2025")  # False
```

### **3️ RegexEmailValidator[T]**

Validates email format using a regex pattern.
Uses a default pattern, but you can pass your own.

```python
from univalidator.validators import RegexEmailValidator

validator = RegexEmailValidator[str]()
validator.validate("user@example.com")  # True
validator.validate("invalid-email")     # False
```

### **4️ MXEmailRecordValidator[T]**

Checks if an email’s domain has MX DNS records.

```python
from univalidator.validators import MXEmailRecordValidator

validator = MXEmailRecordValidator[str]()
validator.validate("user@gmail.com")  # True
validator.validate("user@no-such-domain.com")  # False
```

Restrict to specific domains:

```python
validator = MXEmailRecordValidator[str](allowed_domains=["example.com", "gmail.com"])
```

### **5️ CompositeValidator[T]**

Runs multiple validators in sequence.
All validators must pass for the data to be valid.

```python
from univalidator.composites import CompositeValidator
from univalidator.validators import RegexEmailValidator, MXEmailRecordValidator

validator = CompositeValidator[str]([
    RegexEmailValidator(),
    MXEmailRecordValidator()
])

validator.validate("user@gmail.com")  # True
```

## 🧪 Testing

```bash
uv add pytest
uv run pytest tests
```

## 🌟 Example: Full Email Validation

```python
from univalidator.composites import CompositeValidator
from univalidator.validators import RegexEmailValidator, MXEmailRecordValidator

validator = CompositeValidator[str]([
    RegexEmailValidator(),
    MXEmailRecordValidator()
])

email = "test@gmail.com"
if validator.validate(email):
    print("Valid email with active domain!")
else:
    print("Invalid email.")
```

## 🛠️ Planned Features

- 🔒 Add more Validators

## 🤝 Contributing

Contributions are welcome! Please open an issue or PR for any improvements.

## 📜 License

MIT License — See [LICENSE](LICENSE).

## 👤 Author

For questions or assistance, contact **Shailesh** at [shaileshpandit141@gmail.com](mailto:shaileshpandit141@gmail.com).
