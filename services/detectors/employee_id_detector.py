import re

from config.constants import (
    RISK_MEDIUM,
    TYPE_EMPLOYEE_ID,
)
from models.finding import Finding
from utils.regex_patterns import EMPLOYEE_ID_PATTERN


def detect_employee_ids(text: str) -> list[Finding]:
    employee_ids = set(re.findall(EMPLOYEE_ID_PATTERN, text))

    return [
        Finding(
            type=TYPE_EMPLOYEE_ID,
            value=employee_id,
            risk=RISK_MEDIUM,
        )
        for employee_id in employee_ids
    ]