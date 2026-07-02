from models.finding import Finding

from services.detectors.email_detector import detect_emails
from services.detectors.phone_detector import detect_phone_numbers
from services.detectors.pan_detector import detect_pan
from services.detectors.aadhar_detector import detect_aadhaar
from services.detectors.credit_card_detector import detect_credit_cards
from services.detectors.bank_detector import detect_bank_details
from services.detectors.api_key_detector import detect_api_keys
from services.detectors.employee_id_detector import detect_employee_ids
from services.detectors.confidential_detector import detect_confidential_information

def detect_sensitive_data(text: str) -> list[Finding]:
    """
    Detect all supported sensitive data types.
    """

    findings: list[Finding] = []

    findings.extend(detect_emails(text))
    findings.extend(detect_phone_numbers(text))
    findings.extend(detect_pan(text))
    findings.extend(detect_aadhaar(text))
    findings.extend(detect_credit_cards(text))
    findings.extend(detect_bank_details(text))
    findings.extend(detect_api_keys(text))
    findings.extend(detect_employee_ids(text))
    findings.extend(detect_confidential_information(text))

    return findings