import os
import streamlit as st
from dotenv import load_dotenv

from groq import Groq
from modules.helpers import fix_json
from modules.scorer import semantic_similarity, compute_final_score

load_dotenv()

try:
    api_key = st.secrets["GROQ_API_KEY"]
except Exception:
    api_key = os.getenv("GROQ_API_KEY")

client = Groq(api_key=api_key)

# Build input prompt for Llama 3
def build_prompt(jd_text, resume_text):
    return f"""
You are a Senior Technical Recruiter with 15+ years of hiring experience.

Your task is to compare the Resume with the Job Description and score the candidate realistically.

SCORING RULES:

Skill Match (0-100)
- 90-100 = Candidate matches almost every required skill.
- 70-89 = Candidate matches most required skills.
- 50-69 = Candidate matches around half.
- 20-49 = Candidate has few relevant skills.
- 0-19 = Almost no matching skills.

Experience Match (0-100)
- Score based on relevant projects, internships, work experience, technologies used, certifications and education.
- Freshers with excellent relevant projects should receive between 60 and 80.
- Experienced candidates may receive 80-100.

Return ONLY valid JSON.

{{
    "skill_match": 85,
    "experience_match": 72,
    "fit_level":"Excellent",
    "strengths":[
        "..."
    ],
    "gaps":[
        "..."
    ],
    "recommendation":"Highly Recommended",
    "summary":"..."
}}

JOB DESCRIPTION
----------------
{jd_text}

RESUME
----------------
{resume_text}
"""

# Main function to screen one resume
def screen_resume(jd_text, resume_text):

    prompt = build_prompt(jd_text, resume_text)

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2
    )

    raw = response.choices[0].message.content

    data = fix_json(raw)

    # -------------------------
    # LLM Scores
    # -------------------------

    skill = max(
        0,
        min(100, data.get("skill_match", 0))
    )

    experience = max(
        0,
        min(100, data.get("experience_match", 0))
    )

    # -------------------------
    # REAL NLP Similarity
    # -------------------------

    semantic_score = semantic_similarity(
        jd_text,
        resume_text
    )

    # -------------------------
    # Weighted Final Score
    # -------------------------

    final_score = compute_final_score(
        skill,
        experience,
        semantic_score
    )

    data["semantic_score"] = semantic_score
    data["final_score"] = final_score

    return data