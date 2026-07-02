import re

from config.constants import (
    RISK_HIGH,
    TYPE_API_KEY,
    TYPE_PASSWORD,
)
from models.finding import Finding
from utils.regex_patterns import (
    AWS_API_KEY_PATTERN,
    PASSWORD_PATTERN,
)


def detect_api_keys(text: str) -> list[Finding]:
    findings = []

    api_keys = set(re.findall(AWS_API_KEY_PATTERN, text))
    passwords = set(re.findall(PASSWORD_PATTERN, text))

    findings.extend(
        Finding(
            type=TYPE_API_KEY,
            value=key,
            risk=RISK_HIGH,
        )
        for key in api_keys
    )

    findings.extend(
        Finding(
            type=TYPE_PASSWORD,
            value=password,
            risk=RISK_HIGH,
        )
        for password in passwords
    )

    return findings