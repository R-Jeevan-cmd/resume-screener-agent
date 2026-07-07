# 🤖 AI Resume Screener Agent

> **AI-powered Resume Screening & Candidate Ranking System** built for the **Rooman AI – Junior AI Research Associate (24-Hour AI Agent Challenge)**.

The AI Resume Screener Agent automatically evaluates and ranks multiple resumes against a Job Description (JD) using **Groq Llama 3.1** and **Sentence Transformers**.

Instead of simple keyword matching, the agent combines **LLM reasoning** with **semantic similarity (embeddings)** to produce transparent candidate rankings, hiring recommendations, strengths, skill gaps, and downloadable reports.

---

# 🚀 Features

## 📄 Resume Processing

- Upload Job Description (Text or PDF)
- Upload multiple resumes (PDF)
- Automatic PDF text extraction
- AI-powered resume evaluation
- Handles multiple resumes in one run

---

## 🧠 AI Capabilities

- Skill Match Score
- Experience Match Score
- Semantic Similarity Score
- Weighted Final Score
- Candidate Ranking
- AI-generated Strengths
- AI-generated Skill Gaps
- Hiring Recommendation
- HR Summary

---

# 📊 Dashboard

The Streamlit dashboard provides:

- 👥 Total Candidates
- 📈 Average Score
- 🏆 Highest Score
- ✅ Recommended Candidates

It also displays:

- Ranked Candidate Table
- Individual Candidate Reports
- Score Distribution Chart
- Downloadable Ranked CSV

---

# 🧮 Scoring Methodology

Unlike traditional ATS systems that rely only on keyword matching, this project combines **LLM reasoning** with **embedding-based semantic similarity**.

## Weighted Formula

```
Final Score =
50% Skill Match
+30% Experience Match
+20% Semantic Similarity
```

---

## Semantic Similarity

Uses:

- Sentence Transformers
- Model: all-MiniLM-L6-v2
- Cosine Similarity

This enables matching based on **meaning**, not just exact keywords.

---

# 🧠 AI Workflow

```
                Job Description
                       │
                       ▼
              Resume Upload (PDFs)
                       │
                       ▼
             PDF Text Extraction
                       │
                       ▼
            Groq Llama 3.1 Analysis
                       │
      ┌────────────────┼────────────────┐
      │                │                │
 Skill Match    Experience Match   Strengths & Gaps
      │                │                │
      └────────────────┼────────────────┘
                       │
                       ▼
      Sentence Transformer Embeddings
                       │
                       ▼
          Semantic Similarity Score
                       │
                       ▼
            Weighted Final Scoring
                       │
                       ▼
            Candidate Ranking Engine
                       │
                       ▼
          Streamlit Recruitment Dashboard
                       │
                       ▼
               CSV Report Generation
```

---

# 🛠 Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python 3 |
| Frontend | Streamlit |
| LLM | Groq Llama 3.1 |
| NLP | Sentence Transformers |
| Similarity | Cosine Similarity |
| Machine Learning | scikit-learn |
| PDF Parsing | PyPDF2 |
| Data Processing | pandas |
| Visualization | matplotlib |

---

# 📂 Project Structure

```
resume-screener-agent/

│── app.py
│── resume_screener.py
│── utils.py
│── requirements.txt
│── README.md
│── .env.example
│
├── assets/
│   └── architecture.png
│
├── data/
│   ├── sample_jd/
│   └── sample_resumes/
│
├── modules/
│   ├── parser.py
│   ├── scorer.py
│   └── helpers.py
│
├── output/
│   └── sample_ranked_candidates.csv
│
└── screenshots/
```

---

# ⚙️ Installation

## 1. Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/resume-screener-agent.git

cd resume-screener-agent
```

---

## 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 3. Configure Environment Variables

Create a `.env` file.

```env
GROQ_API_KEY=your_groq_api_key
```

---

## 4. Run the Application

```bash
streamlit run app.py
```

The application opens automatically in your browser.

---

# 📋 Sample Workflow

1. Upload a Job Description.
2. Upload one or more candidate resumes.
3. AI analyzes every resume.
4. Semantic similarity is calculated.
5. Weighted scores are computed.
6. Candidates are ranked.
7. Download the ranked CSV report.

---

# 📤 Output

For every candidate, the system generates:

- Final Score
- Skill Match
- Experience Match
- Semantic Similarity
- Fit Level
- Strengths
- Skill Gaps
- Recommendation
- AI Summary

The application also exports:

```
ranked_candidates.csv
```

---

# 🎯 Design Decisions

### Why Groq Llama 3.1?

- Fast inference
- High-quality reasoning
- Low latency
- Cost effective

### Why Sentence Transformers?

Traditional keyword matching fails when wording differs.

Sentence Transformers compare the **meaning** between resumes and the Job Description, resulting in more reliable candidate ranking.

### Why Combine Both?

The LLM provides:

- HR reasoning
- Strengths
- Skill gaps
- Hiring recommendation

Sentence Transformers provide:

- Objective semantic similarity

Combining both produces more explainable and consistent rankings.

---

# ⚠️ Limitations

- Supports text-based PDF resumes.
- Scanned PDFs require OCR.
- LLM responses may vary slightly.
- Sequential processing for simplicity.

---

# 🚀 Future Improvements

- DOCX support
- OCR for scanned resumes
- FAISS / ChromaDB integration
- ATS Integration
- Batch processing
- Interview Question Generator
- Email Notifications
- Recruiter Analytics Dashboard
- Multi-role Resume Comparison

---

# 📸 Screenshots

Include screenshots inside the `screenshots/` folder.

Example:

- Home Page
- Resume Upload
- Ranked Candidates
- Candidate Reports
- Dashboard
- CSV Export

---

# 🌐 Live Demo

https://resume-screener-agent-a3l4nho4fx5btnx9vrsnba.streamlit.app

---

# 📄 Challenge Deliverables

✔ Working AI Resume Screening Agent

✔ Multiple Resume Support

✔ Job Description Matching

✔ Semantic NLP Similarity

✔ Candidate Ranking

✔ CSV Export

✔ Public GitHub Repository

✔ Sample Inputs

✔ Sample Outputs

✔ README Documentation

✔ Design Trade-offs

---

# 👨‍💻 Author

**R Jeevan**

B.E. Computer Science & Engineering (AI & ML)

Built for the **Rooman AI – Junior AI Research Associate (24-Hour AI Agent Challenge)**.