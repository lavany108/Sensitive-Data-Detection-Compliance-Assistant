from config.constants import (
    RISK_HIGH,
    TYPE_CONFIDENTIAL,
)
from models.finding import Finding


CONFIDENTIAL_KEYWORDS = [
    "confidential",
    "internal use only",
    "trade secret",
    "proprietary",
    "do not distribute",
    "nda",
]


def detect_confidential_information(text: str) -> list[Finding]:
    findings = []

    lower_text = text.lower()

    for keyword in CONFIDENTIAL_KEYWORDS:
        if keyword in lower_text:
            findings.append(
                Finding(
                    type=TYPE_CONFIDENTIAL,
                    value=keyword,
                    risk=RISK_HIGH,
                )
            )

    return findings