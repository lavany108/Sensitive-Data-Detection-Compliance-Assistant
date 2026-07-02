import os

import google.generativeai as genai
from dotenv import load_dotenv

from config.prompts import SUMMARY_PROMPT
from models.finding import Finding

# Load environment variables
load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Create the model
model = genai.GenerativeModel("gemini-2.5-flash")


def generate_summary(
    text: str,
    findings: list[Finding],
) -> str:
    """
    Generate an AI-powered compliance and security summary.
    """

    if not text.strip():
        return "No document text available."

    if findings:
        findings_text = "\n".join(
            f"- {finding.type}: {finding.value} (Risk: {finding.risk})"
            for finding in findings
        )
    else:
        findings_text = "No sensitive data detected."

    prompt = SUMMARY_PROMPT.format(
        findings=findings_text,
        text=text,
    )

    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        return f"Error generating AI summary:\n\n{e}"