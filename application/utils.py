import hashlib
from datetime import datetime, timezone

from exceptions import InvalidTypeProvided


def generate_sign(sign_bytes_string: bytes) -> str:
    """Generates sign for payments"""

    try:
        return hashlib.sha256(sign_bytes_string).hexdigest()
    except TypeError as exc:
        raise InvalidTypeProvided(
            f"Invalid sign byte string provided: {sign_bytes_string}, exception: {exc}")


def get_utc_now():
    """Gets current datetime in UTC"""

    return datetime.now(timezone.utc)
