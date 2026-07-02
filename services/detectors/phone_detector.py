import re

from config.constants import (
    RISK_MEDIUM,
    TYPE_PHONE,
)
from models.finding import Finding
from utils.regex_patterns import PHONE_PATTERN


def detect_phone_numbers(text: str) -> list[Finding]:
    """
    Detect Indian phone numbers.
    """

    phones = set(re.findall(PHONE_PATTERN, text))

    return [
        Finding(
            type=TYPE_PHONE,
            value=phone,
            risk=RISK_MEDIUM,
        )
        for phone in phones
    ]