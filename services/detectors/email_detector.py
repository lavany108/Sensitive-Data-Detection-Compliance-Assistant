from config.constants import (
    RISK_MEDIUM,
    TYPE_EMAIL,
)

from models.finding import Finding
from utils.regex_patterns import EMAIL_PATTERN

import re


def detect_emails(text: str) -> list[Finding]:
    emails = set(re.findall(EMAIL_PATTERN, text))

    return [
        Finding(
            type=TYPE_EMAIL,
            value=email,
            risk=RISK_MEDIUM,
        )
        for email in emails
    ]