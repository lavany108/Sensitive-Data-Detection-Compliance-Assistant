import os

import google.generativeai as genai
from dotenv import load_dotenv

from config.prompts import QA_PROMPT
from models.finding import Finding

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


def answer_question(
    text: str,
    findings: list[Finding],
    question: str,
) -> str:
    """
    Answer questions about the uploaded document.
    """

    if not question.strip():
        return "Please enter a question."

    if findings:
        findings_text = "\n".join(
            f"- {finding.type}: {finding.value} (Risk: {finding.risk})"
            for finding in findings
        )
    else:
        findings_text = "No sensitive data detected."

    prompt = QA_PROMPT.format(
        findings=findings_text,
        text=text,
        question=question,
    )

    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        return f"Error answering question:\n\n{e}"