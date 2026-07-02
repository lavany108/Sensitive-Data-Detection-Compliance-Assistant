import streamlit as st
from services.parser import extract_text

st.set_page_config(
    page_title="Sensitive Data Detection & Compliance Assistant",
    page_icon="🛡️",
    layout="wide",
)

st.title("🛡️ Sensitive Data Detection & Compliance Assistant")

st.markdown(
    """
    Upload a document to analyze sensitive information and compliance risks.

    **Supported file types:**
    - 📄 PDF
    - 📝 TXT
    - 📊 CSV
    """
)

uploaded_file = st.file_uploader(
    "Choose a document",
    type=["pdf", "txt", "csv"],
)

if uploaded_file:
    try:
        # Extract text and metadata
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
            label="Content",
            value=text,
            height=350,
        )

    except Exception as e:
        st.error(f"Error processing file: {e}")