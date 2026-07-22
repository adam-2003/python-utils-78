from typing import Any, Optional


def is_valid_email(email: str) -> bool:
    """Validate an email address format."""
    import re
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(pattern, email) is not None


def is_positive_integer(value: Any) -> Optional[bool]:
    """Check if the value is a positive integer."""
    if isinstance(value, int) and value > 0:
        return True
    return False


def is_not_empty_string(value: Any) -> bool:
    """Check if the value is a non-empty string."""
    return isinstance(value, str) and bool(value.strip())


def validate_user_data(email: str, age: Any) -> bool:
    """Validate user data fields: email and age."""
    return is_valid_email(email) and is_positive_integer(age)