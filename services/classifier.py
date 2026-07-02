from models.finding import Finding
from config.constants import (
    RISK_LOW,
    RISK_MEDIUM,
    RISK_HIGH,
)


def classify_document(findings: list[Finding]) -> str:
    """
    Classify the overall document risk based on detected findings.
    """

    if not findings:
        return RISK_LOW

    risks = {finding.risk for finding in findings}

    if RISK_HIGH in risks:
        return RISK_HIGH

    if RISK_MEDIUM in risks:
        return RISK_MEDIUM

    return RISK_LOW