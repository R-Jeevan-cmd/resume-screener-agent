import streamlit as st
import pandas as pd
from utils import extract_pdf_text
from resume_screener import screen_resume

st.set_page_config(page_title="AI Resume Screener", layout="wide")

st.title("🤖 AI Resume Screener Agent")
st.write("Upload a job description and multiple resumes to generate ranked candidate evaluations.")

# --- JD Upload ---
st.header("1️⃣ Upload Job Description")
jd_text = st.text_area("Paste Job Description", height=200)

jd_file = st.file_uploader("Or upload JD PDF", type=["pdf"])
if jd_file:
    jd_text = extract_pdf_text(jd_file)

# --- Resume Upload ---
st.header("2️⃣ Upload Candidate Resumes (PDF)")
resume_files = st.file_uploader(
    "Choose 1 or more PDF resumes",
    type=["pdf"],
    accept_multiple_files=True
)

# --- Run Screening ---
if st.button("🔍 Screen Resumes"):
    if not jd_text:
        st.error("Please provide a Job Description first.")
    elif not resume_files:
        st.error("Please upload at least one resume.")
    else:
        st.success("Processing resumes...")

        results = []

        for file in resume_files:
            resume_text = extract_pdf_text(file)
            data = screen_resume(jd_text, resume_text)

            results.append({
                "Candidate File": file.name,
                "Final Score": data["final_score"],
                "Fit Level": data["fit_level"],
                "Strengths": ", ".join(data["strengths"]),
                "Gaps": ", ".join(data["gaps"]),
                "Recommendation": data["recommendation"],
                "Summary": data["summary"]
            })

        df = pd.DataFrame(results).sort_values("Final Score", ascending=False)
        df.index = range(1, len(df) + 1)
        df.index.name = "Rank"

        st.subheader("📊 Ranked Candidates")
        st.dataframe(df)

        # Download CSV
        csv = df.to_csv().encode("utf-8")
        st.download_button("📥 Download CSV", csv, "ranked_candidates.csv")

        # Detailed reports
        st.subheader("📄 Candidate Reports")
        for idx, row in df.iterrows():
            with st.expander(f"{idx}. {row['Candidate File']}  —  {row['Final Score']}"):
                st.write(f"**Fit Level:** {row['Fit Level']}")
                st.write(f"**Recommendation:** {row['Recommendation']}")
                st.write(f"**Strengths:** {row['Strengths']}")
                st.write(f"**Gaps:** {row['Gaps']}")
                st.write(f"**Summary:** {row['Summary']}")

# Footer
st.markdown("---")
st.caption("Built by Jeevan • AI Resume Screener Agent • Powered by Groq Llama 3")