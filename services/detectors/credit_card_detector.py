import re

from config.constants import (
    RISK_HIGH,
    TYPE_CREDIT_CARD,
)
from models.finding import Finding
from utils.regex_patterns import CREDIT_CARD_PATTERN


def detect_credit_cards(text: str) -> list[Finding]:
    """
    Detect credit card numbers.
    """

    cards = set(re.findall(CREDIT_CARD_PATTERN, text))

    return [
        Finding(
            type=TYPE_CREDIT_CARD,
            value=card,
            risk=RISK_HIGH,
        )
        for card in cards
    ]