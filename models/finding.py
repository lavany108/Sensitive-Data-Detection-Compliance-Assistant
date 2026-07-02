from dataclasses import dataclass


@dataclass(frozen=True)
class Finding:
    """
    Represents a single sensitive data finding.
    """

    type: str
    value: str
    risk: str