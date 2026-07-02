# 🛡️ Sensitive Data Detection & Compliance Assistant

An AI-powered document analysis application that detects sensitive information, classifies compliance risk, generates security insights, and answers questions about uploaded documents.

Built as part of a technical assessment.

---

# Features

## 📄 Document Upload

Supports:

- PDF
- TXT
- CSV

Documents are automatically parsed and converted into text for further analysis.

---

## 🔍 Sensitive Data Detection

The application detects the following information using modular regex-based detectors:

- Aadhaar Numbers
- PAN Numbers
- Email Addresses
- Phone Numbers
- Credit Card Numbers
- Bank Account Numbers
- IFSC Codes
- API Keys
- Passwords
- Employee IDs
- Confidential Business Information

---

## 🚨 Risk Classification

Detected findings are used to classify the overall document risk into:

- 🟢 Low
- 🟠 Medium
- 🔴 High

---

## 🤖 AI Compliance Summary

Using Google Gemini, the application generates:

- Executive Summary
- Compliance Observations
- Security Risks
- Suggested Remediation Steps

---

## 💬 Question Answering

Users can ask natural language questions about the uploaded document.

Examples:

- What sensitive data exists in the document?
- How many email addresses are present?
- Summarize this document.
- What compliance risks are identified?
- Does this document contain confidential information?

---

# Tech Stack

- Python 3.12
- Streamlit
- Google Gemini API
- PyMuPDF
- Pandas
- Regular Expressions (Regex)

---

# Project Structure

```
Sensitive-Data-Detection-Compliance-Assistant/

├── app.py
├── config/
│   ├── constants.py
│   └── prompts.py
│
├── models/
│   └── finding.py
│
├── services/
│   ├── parser.py
│   ├── detector.py
│   ├── classifier.py
│   ├── summarizer.py
│   ├── qa.py
│   └── detectors/
│       ├── email_detector.py
│       ├── phone_detector.py
│       ├── pan_detector.py
│       ├── aadhar_detector.py
│       ├── credit_card_detector.py
│       ├── bank_detector.py
│       ├── api_key_detector.py
│       ├── employee_id_detector.py
│       └── confidential_detector.py
│
├── utils/
│   └── regex_patterns.py
│
├── sample_docs/
├── tests/
├── requirements.txt
└── README.md
```

---

# Installation

Clone the repository.

```bash
git clone https://github.com/lavany108/Sensitive-Data-Detection-Compliance-Assistant.git

cd Sensitive-Data-Detection-Compliance-Assistant
```

Create a virtual environment.

```bash
python -m venv venv
```

Activate it.

macOS/Linux

```bash
source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

Install dependencies.

```bash
pip install -r requirements.txt
```

Create a `.env` file.

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

Run the application.

```bash
python -m streamlit run app.py
```

---

# Design Decisions

The application follows a modular architecture to improve maintainability and scalability.

- Parsing logic is separated from detection logic.
- Each sensitive data type has its own detector module.
- Risk classification is isolated into a dedicated service.
- AI summarization and Question Answering are implemented as independent services.
- Regex patterns are centralized for easy maintenance.
- Streamlit is used as the presentation layer while business logic remains inside service modules.

This structure allows additional detectors and AI features to be added with minimal changes to the existing codebase.

---

# Challenges Encountered

During development, the following challenges were addressed:

- Parsing multiple document formats (PDF, TXT, CSV)
- Designing modular detectors instead of a single large detection file
- Managing Streamlit reruns using `st.session_state`
- Integrating Google Gemini for both summarization and question answering
- Balancing detection accuracy while minimizing false positives
- Organizing the project into reusable service modules

---

# AI Usage Disclosure

Artificial Intelligence tools were used during development for:

- brainstorming architecture ideas
- improving code organization
- generating prompt templates
- debugging implementation issues
- refining documentation

All code was reviewed, integrated, tested, and modified manually before inclusion in the final project.

---

# Future Improvements

- Data masking / automatic redaction
- OCR support for scanned PDFs
- Additional compliance frameworks
- More advanced PII detection using NLP
- Export reports as PDF
- User authentication
- Audit logs
- Batch document processing

---

# Author

Lavanya

B.Tech Computer Science (AI & ML)

GLA University

---

# Repository

https://github.com/lavany108/Sensitive-Data-Detection-Compliance-Assistant