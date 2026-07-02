import re

from config.constants import RISK_HIGH, TYPE_PAN
from models.finding import Finding
from utils.regex_patterns import PAN_PATTERN


def detect_pan(text: str) -> list[Finding]:
    pans = set(re.findall(PAN_PATTERN, text))

    return [
        Finding(
            type=TYPE_PAN,
            value=pan,
            risk=RISK_HIGH,
        )
        for pan in pans
    ]