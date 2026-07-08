import streamlit as st
import pandas as pd
import time
import matplotlib.pyplot as plt

from modules.helpers import extract_pdf_text
from resume_screener import screen_resume

st.set_page_config(
    page_title="AI Resume Screener",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Resume Screener Agent")
st.markdown(
    "Upload a **Job Description** and **multiple resumes** to automatically rank candidates using AI."
)

st.divider()

# -------------------------
# Job Description
# -------------------------

st.header("📄 Step 1: Upload Job Description")

jd_text = st.text_area(
    "Paste Job Description",
    height=220
)

jd_file = st.file_uploader(
    "Or Upload JD PDF",
    type=["pdf"]
)

if jd_file:
    jd_text = extract_pdf_text(jd_file)

# -------------------------
# Resume Upload
# -------------------------

st.header("📁 Step 2: Upload Candidate Resumes")

resume_files = st.file_uploader(
    "Upload one or more PDF resumes",
    type=["pdf"],
    accept_multiple_files=True
)

# -------------------------
# Screening
# -------------------------

if st.button("🚀 Screen Resumes", width="stretch"):

    if not jd_text.strip():
        st.error("Please provide a Job Description.")
        st.stop()

    if not resume_files:
        st.error("Please upload at least one resume.")
        st.stop()

    progress = st.progress(0)
    status = st.empty()

    results = []

    total = len(resume_files)

    for i, file in enumerate(resume_files):

        status.info(f"📄 Processing {file.name} ({i+1}/{total})...")

        resume_text = extract_pdf_text(file)
        data = screen_resume(jd_text, resume_text)

        results.append({
            "Candidate": file.name,
            "Final Score": round(float(data["final_score"]), 1),
            "Fit Level": data["fit_level"],
            "Strengths": ", ".join(data["strengths"]),
            "Gaps": ", ".join(data["gaps"]),
            "Recommendation": data["recommendation"],
            "Summary": data["summary"]
        })

        progress.progress((i + 1) / total)

    status.success("✅ Screening Complete!")
    st.balloons()

    df = (
        pd.DataFrame(results)
        .sort_values("Final Score", ascending=False)
        .reset_index(drop=True)
    )

    # Rank
    df.index += 1
    df.index.name = "Rank"

    # -------------------------
    # Metrics
    # -------------------------

    st.divider()

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "👥 Candidates",
        len(df)
    )

    col2.metric(
        "📈 Average Score",
        f"{df['Final Score'].mean():.1f}"
    )

    col3.metric(
        "🏆 Top Score",
        f"{df['Final Score'].max():.1f}"
    )

    recommended = (
        df["Recommendation"]
        .str.contains("Recommend", case=False, na=False)
        .sum()
    )

    col4.metric(
        "✅ Recommended",
        recommended
    )

    st.divider()

    st.subheader("🏆 Ranked Candidates")

    # Display only the most important columns
    display_df = df[
        [
            "Candidate",
            "Final Score",
            "Fit Level",
            "Recommendation",
        ]
    ].copy()

    st.dataframe(
        display_df,
        width="stretch"
    )

    st.subheader("📊 Candidate Score Distribution")

    fig, ax = plt.subplots(figsize=(8, 4))

    colors = ["#FFD700"] + ["#4F81BD"] * (len(display_df) - 1)

    ax.bar(
        display_df["Candidate"],
        display_df["Final Score"],
        color=colors
    )

    ax.set_ylabel("Final Score")
    ax.set_xlabel("Candidates")
    ax.set_title("Candidate Ranking Scores")
    ax.set_ylim(0, 100)

    for i, score in enumerate(display_df["Final Score"]):
        ax.text(
            i,
            score + 1,
            f"{score:.1f}",
            ha="center",
            fontsize=9
        )

    plt.xticks(rotation=20, ha="right")

    st.pyplot(fig)

    # Export the complete report
    csv = df.to_csv(index=True).encode("utf-8")

    st.download_button(
        "📥 Download Ranked CSV",
        csv,
        "ranked_candidates.csv",
        "text/csv"
    )

    st.divider()

    st.subheader("📄 Candidate Reports")

    medals = ["🥇", "🥈", "🥉"]

    for idx, row in df.iterrows():

        medal = medals[idx-1] if idx <= 3 else "🏅"

        with st.expander(
            f"{medal} Rank {idx} • {row['Candidate']} • Score {row['Final Score']}"
        ):

            fit = row["Fit Level"]

            if fit.lower() == "excellent":
                st.success(f"Fit Level: {fit}")
            elif fit.lower() == "good":
                st.info(f"Fit Level: {fit}")
            else:
                st.warning(f"Fit Level: {fit}")

            st.markdown("### ⭐ Strengths")
            st.write(row["Strengths"])

            st.markdown("### ⚠ Skill Gaps")
            st.write(row["Gaps"])

            st.markdown("### 💡 Recommendation")
            st.write(row["Recommendation"])

            st.markdown("### 📝 AI Summary")
            st.write(row["Summary"])

st.divider()
st.caption("Built by R Jeevan • AI Resume Screener Agent • Powered by Groq Llama 3 + Sentence Transformers (Semantic NLP)")