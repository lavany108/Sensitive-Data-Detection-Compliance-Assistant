import re

from config.constants import (
    RISK_HIGH,
    TYPE_AADHAAR,
)
from models.finding import Finding
from utils.regex_patterns import AADHAAR_PATTERN


def detect_aadhaar(text: str) -> list[Finding]:
    """
    Detect Aadhaar numbers.
    """

    aadhaar_numbers = set(re.findall(AADHAAR_PATTERN, text))

    return [
        Finding(
            type=TYPE_AADHAAR,
            value=aadhaar,
            risk=RISK_HIGH,
        )
        for aadhaar in aadhaar_numbers
    ]