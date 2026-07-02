import pandas as pd
import streamlit as st

from services.classifier import classify_document
from services.detector import detect_sensitive_data
from services.parser import extract_text
from services.qa import answer_question
from services.summarizer import generate_summary

st.set_page_config(
    page_title="Sensitive Data Detection & Compliance Assistant",
    page_icon="💼",
    layout="wide",
)

# -------------------------
# Session State
# -------------------------
if "findings" not in st.session_state:
    st.session_state.findings = []

if "document_risk" not in st.session_state:
    st.session_state.document_risk = None

if "summary" not in st.session_state:
    st.session_state.summary = None

st.title("💼 Sensitive Data Detection & Compliance Assistant")

st.markdown(
    """
Upload a document to analyze sensitive information and compliance risks.

**Supported file types**
- PDF
- TXT
- CSV
"""
)

uploaded_file = st.file_uploader(
    "Choose a document",
    type=["pdf", "txt", "csv"],
)

if uploaded_file:

    try:

        # -------------------------
        # Extract text
        # -------------------------
        text, metadata = extract_text(uploaded_file)

        st.success("Document uploaded successfully!")

        st.subheader("Document Information")

        col1, col2 = st.columns(2)

        with col1:
            st.write(f"**Filename:** {uploaded_file.name}")
            st.write(f"**Type:** {metadata['type']}")

        with col2:
            st.write(f"**Size:** {uploaded_file.size:,} bytes")

            if metadata["type"] == "PDF":
                st.write(f"**Pages:** {metadata['pages']}")

            elif metadata["type"] == "CSV":
                st.write(f"**Rows:** {metadata['rows']}")
                st.write(f"**Columns:** {metadata['columns']}")

            st.write(f"**Characters:** {metadata['characters']:,}")

        st.divider()

        st.subheader("Extracted Text Preview")

        st.text_area(
            "Content",
            value=text,
            height=300,
        )

        st.divider()

        # -------------------------
        # Analyze Button
        # -------------------------
        if st.button(
            "Analyze Document",
            type="primary",
            use_container_width=False,
        ):

            with st.spinner("Analyzing document..."):

                st.session_state.findings = detect_sensitive_data(text)

                st.session_state.document_risk = classify_document(
                    st.session_state.findings
                )

                st.session_state.summary = generate_summary(
                    text,
                    st.session_state.findings,
                )

        # -------------------------
        # Show Results
        # -------------------------
        if st.session_state.findings:

            st.subheader("Detection Results")

            rows = [
                {
                    "Type": finding.type,
                    "Value": finding.value,
                    "Risk": finding.risk,
                }
                for finding in st.session_state.findings
            ]

            df = pd.DataFrame(rows)

            st.dataframe(
                df,
                use_container_width=True,
                hide_index=True,
            )

            # -------------------------
            # Metrics
            # -------------------------
            col1, col2 = st.columns(2)

            with col1:
                st.metric(
                    "Sensitive Items Found",
                    len(st.session_state.findings),
                )

            with col2:
                high_risk = sum(
                    finding.risk == "High"
                    for finding in st.session_state.findings
                )

                st.metric(
                    "High Risk Items",
                    high_risk,
                )

            # -------------------------
            # Overall Risk
            # -------------------------
            st.subheader("Overall Risk Classification")

            risk_icon = {
                "Low": "🟢",
                "Medium": "🟠",
                "High": "🔴",
            }

            st.info(
                f"{risk_icon[st.session_state.document_risk]} "
                f"**{st.session_state.document_risk} Risk**"
            )

            # -------------------------
            # AI Summary
            # -------------------------
            st.subheader("AI Compliance & Security Summary")

            st.markdown(st.session_state.summary)

            st.divider()

            # -------------------------
            # Question Answering
            # -------------------------
            st.subheader("Ask Questions About the Document")

            question = st.text_input(
                "Enter your question",
                placeholder="e.g. What sensitive data exists in the document?",
            )

            if st.button("Ask Question"):

                if question.strip():

                    with st.spinner("Generating answer..."):

                        answer = answer_question(
                            text,
                            st.session_state.findings,
                            question,
                        )

                    st.markdown("### Answer")

                    st.write(answer)

                else:
                    st.warning("Please enter a question.")

    except Exception as e:
        st.error(f"Error processing file:\n\n{e}")