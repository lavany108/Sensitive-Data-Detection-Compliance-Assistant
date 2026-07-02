from pathlib import Path
from typing import Any

import fitz  # PyMuPDF
import pandas as pd


def extract_text(uploaded_file: Any) -> tuple[str, dict]:
    """
    Extract text and metadata from an uploaded document.

    Supported formats:
    - PDF
    - TXT
    - CSV

    Returns:
        tuple[str, dict]: Extracted text and metadata.
    """

    extension = Path(uploaded_file.name).suffix.lower()

    match extension:
        case ".txt":
            return _extract_txt(uploaded_file)

        case ".pdf":
            return _extract_pdf(uploaded_file)

        case ".csv":
            return _extract_csv(uploaded_file)

        case _:
            raise ValueError(f"Unsupported file type: {extension}")


def _extract_txt(uploaded_file: Any) -> tuple[str, dict]:
    """Extract text from a TXT file."""

    text = uploaded_file.read().decode("utf-8", errors="ignore")

    metadata = {
        "type": "TXT",
        "characters": len(text),
    }

    return text, metadata


def _extract_pdf(uploaded_file: Any) -> tuple[str, dict]:
    """Extract text from a PDF file."""

    with fitz.open(stream=uploaded_file.read(), filetype="pdf") as doc:
        text = ""

        for page in doc:
            text += page.get_text()

        metadata = {
            "type": "PDF",
            "pages": len(doc),
            "characters": len(text),
        }

    return text, metadata


def _extract_csv(uploaded_file: Any) -> tuple[str, dict]:
    """Extract text from a CSV file."""

    df = pd.read_csv(uploaded_file)

    text = df.to_string(index=False)

    metadata = {
        "type": "CSV",
        "rows": len(df),
        "columns": len(df.columns),
        "characters": len(text),
    }

    return text, metadata