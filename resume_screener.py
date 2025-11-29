import os
from dotenv import load_dotenv
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), ".env"))

from groq import Groq
from utils import fix_json, extract_pdf_text

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Build input prompt for Llama 3
def build_prompt(jd_text, resume_text):
    return f"""
You are an AI resume screening expert.

Compare this Resume with this Job Description and return ONLY valid JSON:

JOB DESCRIPTION:
{jd_text}

RESUME:
{resume_text}

Respond in this JSON format:
{{
  "skill_match": 0-100,
  "experience_match": 0-100,
  "jd_relevance": 0-100,
  "fit_level": "Strong/Medium/Weak",
  "strengths": ["..."],
  "gaps": ["..."],
  "recommendation": "Interview/Hold/Reject",
  "summary": "Short HR explanation"
}}
"""

# Weighted scoring
def compute_final_score(skill, exp, jd):
    score = (0.5 * skill) + (0.3 * exp) + (0.2 * jd)
    return int(round(score))

# Main function to screen one resume
def screen_resume(jd_text, resume_text):
    prompt = build_prompt(jd_text, resume_text)

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role":"user","content":prompt}],
        temperature=0.3
    )
    
    raw = response.choices[0].message.content
    data = fix_json(raw)

    # Clamp numeric values
    skill = max(0, min(100, data.get("skill_match", 0)))
    exp = max(0, min(100, data.get("experience_match", 0)))
    jd_rel = max(0, min(100, data.get("jd_relevance", 0)))

    final_score = compute_final_score(skill, exp, jd_rel)

    data["final_score"] = final_score
    return data