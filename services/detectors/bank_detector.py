import re

from config.constants import (
    RISK_MEDIUM,
    TYPE_BANK_ACCOUNT,
    TYPE_IFSC,
)
from models.finding import Finding
from utils.regex_patterns import (
    BANK_ACCOUNT_PATTERN,
    IFSC_PATTERN,
)


def detect_bank_details(text: str) -> list[Finding]:
    findings = []

    accounts = set(re.findall(BANK_ACCOUNT_PATTERN, text))
    ifsc_codes = set(re.findall(IFSC_PATTERN, text))

    findings.extend(
        Finding(
            type=TYPE_BANK_ACCOUNT,
            value=account,
            risk=RISK_MEDIUM,
        )
        for account in accounts
    )

    findings.extend(
        Finding(
            type=TYPE_IFSC,
            value=code,
            risk=RISK_MEDIUM,
        )
        for code in ifsc_codes
    )

    return findings