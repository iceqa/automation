import random
import string
import datetime
from datetime import timezone


def get_str_with_length(n: int) -> str:
    return ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=n))


def get_current_time_without_tzinfo():
    return datetime.datetime.now(tz=timezone.utc).replace(microsecond=0).isoformat()
