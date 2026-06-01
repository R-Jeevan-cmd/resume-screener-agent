# 🤖 AI Resume Screener Agent

The **AI Resume Screener Agent** automatically evaluates multiple resumes against a given Job Description (JD).  
It uses **Groq Llama 3**, **LangChain**, **Streamlit**, and **Python** to generate:

- Match Score (0–100)
- Fit Level (Strong / Medium / Weak)
- Strengths & Gaps
- Final Recommendation (Interview / Hold / Reject)
- HR-friendly summary explanation
- Ranked shortlist table

This tool reduces hours of manual resume screening and improves consistency in hiring.

---

## 🚀 Features

### ✔ Resume Evaluation
- Skill match score (0–100)  
- Experience match score (0–100)  
- JD relevance (0–100)  
- Fit Level: **Strong / Medium / Weak**  
- Strengths (bullet points)  
- Gaps / missing skills  
- Final recommendation  
- HR summary paragraph  

### ✔ System Features
- Upload **one JD** (text or PDF)
- Upload **multiple resumes** (PDF)
- Ranks candidates automatically
- Download CSV with results
- (Optional) Sync results to Google Sheets

---

## 🧠 Architecture Overview

User → Streamlit UI → Resume + JD → Screening Logic → Groq Llama 3 → Results → Ranking → Display/Export

### 1. **User**
Uploads JD + multiple resumes.

### 2. **Streamlit Frontend**
- Sends text to backend
- Displays ranked results & reports

### 3. **Agent Logic (LangChain + Python)**
- Extracts text from PDFs  
- Builds structured prompt  
- Normalizes JSON output  
- Uses scoring formula  
- Ranks candidates  

### 4. **LLM Layer (Groq Llama 3)**
- Compares resume vs JD  
- Returns structured JSON analysis  

### 5. **Data Layer**
- pandas → ranking table + CSV  
- Optional: Google Sheets  

---

## 🧮 Ranking Formula
Final Score =
(0.5 × Skill Match) +
(0.3 × Experience Match) +
(0.2 × JD Relevance)

This weights **skills** highest, reflecting real-world hiring priorities.

---

## 🧰 Tech Stack

- **Python 3**
- **Streamlit** (UI)
- **Groq Llama 3** (LLM)
- **LangChain** (prompt/agent logic)
- **PyPDF2** (resume extraction)
- **pandas** (tables + CSV)
- **gspread** (optional Google Sheets)
- **chromadb** (future embeddings)

---

## ⚙️ Setup Instructions

### 1. Install dependencies
pip install -r requirements.txt

### 2. Add your Groq key  
Create a `.env` file:
GROQ_API_KEY=your_key_here

### 3. Run the app
streamlit run app.py

---

## 📂 Project Structure

resume-screener/
│── app.py
│── resume_screener.py
│── utils.py
│── requirements.txt
│── README.md
│── sample_resumes/
│── sample_jd/

---

## 📤 Export Options
- Download CSV  
- Optional: Sync to Google Sheets  

---

## 🚧 Limitations
- Very messy PDFs may reduce extraction accuracy  
- Depends on prompt honesty by LLM  
- Not a full Applicant Tracking System  

---

## 🚀 Future Improvements
- Add embeddings (Chroma / FAISS)
- Multi-JD support (multiple roles)
- Automated email notifications  
- ATS integration  

---

https://resume-screener-agent-o4kye9olujldrq4se9zjzb.streamlit.app