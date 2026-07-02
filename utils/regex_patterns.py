"""
Regular expression patterns for detecting sensitive data.
"""

EMAIL_PATTERN = (
    r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
)

PHONE_PATTERN = (
    r"\b(?:\+91[\s-]?)?[6-9]\d{9}\b"
)
# Aadhaar
AADHAAR_PATTERN = r"\b\d{4}\s?\d{4}\s?\d{4}\b"

# PAN
PAN_PATTERN = r"\b[A-Z]{5}[0-9]{4}[A-Z]\b"

# Credit Card
CREDIT_CARD_PATTERN = r"\b(?:\d[ -]?){13,19}\b"

# Bank Account (9–18 digits)
BANK_ACCOUNT_PATTERN = r"\b\d{9,18}\b"

# IFSC
IFSC_PATTERN = r"\b[A-Z]{4}0[A-Z0-9]{6}\b"

# Generic Employee ID
EMPLOYEE_ID_PATTERN = r"\bEMP[0-9]{3,8}\b"

# AWS API Key
AWS_API_KEY_PATTERN = r"\bAKIA[0-9A-Z]{16}\b"

# Generic Password
PASSWORD_PATTERN = (
    r"(?i)\b(?:password|passwd|pwd)\s*[:=]\s*\S+"
)