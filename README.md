# AI-Powered Resume–Job Match & Skill Gap Analyzer

An end-to-end NLP + GenAI application that analyzes how well a resume matches a job description, identifies skill gaps, provides ATS-style feedback, and suggests resume improvements using LLMs.

🔗 GitHub Repository: https://github.com/Anjalinevgi/Resume-jd-skill-gap-analyzer

---

# Features

- Upload resume (PDF) and paste job description
- Semantic match score using sentence embeddings
- Domain-agnostic skill extraction using Groq LLM
- Rule-based validation to identify missing and implicit skills
- ATS-style heuristic feedback (non-ML, explainable)
- LLM-based resume bullet improvement suggestions
- Interactive Streamlit UI
- Dockerized for reproducibility

---

#  How the System Works

# 1. Semantic Matching
- Resume and Job Description are converted into embeddings using **sentence-transformers**
- **Cosine similarity** is used to compute an overall match score

# 2. Skill Gap Analysis (Hybrid Design)
- Groq LLM suggests relevant skills from the job description
- Suggested skills are **validated against the resume text** using:
  - Exact matches
  - Curated synonym mapping
- Skills are categorized as:
  - Matched / Implicit
  - Missing (critical or aspirational)

>  LLMs are **not** used for scoring or decision-making to avoid hallucinations.

# 3. ATS Heuristic Feedback
Simple, explainable checks inspired by common ATS rules:
- Resume length
- Presence of quantifiable metrics
- Bullet-point structure

This is **not a real ATS**, but a transparent heuristic layer.

# 4. Resume Improvement Suggestions
- Groq LLM rewrites resume bullets to better align with the job description
- Guardrails ensure **no fabrication of experience**

---

# Tech Stack

- **Python**
- **Streamlit** – UI
- **Sentence-Transformers** – semantic embeddings
- **Groq (Llama 3.1)** – skill suggestion & resume rewriting
- **Scikit-learn** – similarity computation
- **PDFPlumber** – resume parsing
- **Docker** – containerization

---

#  Project Structure

Resume-jd-skill-gap-analyzer/
│
├── app.py # Streamlit application
├── resume_parser.py # PDF resume text extraction
├── embeddings.py # Embedding & similarity logic
├── llm_skill_suggester.py # LLM-based skill extraction
├── skill_gap.py # Rule-based skill validation
├── ats_rules.py # ATS heuristic checks
├── llm_feedback.py # Resume improvement suggestions
├── requirements.txt
├── Dockerfile
├── .gitignore
├── .dockerignore
└── README.md

Environment Variables

Create a .env file:

GROQ_API_KEY=your_groq_api_key_here
The .env file is excluded via .gitignore.

# Design Decisions & Limitations

LLMs are used only for suggestion and rewriting, not scoring
Skill gap decisions are rule-validated for explainability
ATS feedback is heuristic-based, not a real ATS
Match score represents semantic similarity, not hiring probability

# Use Cases

Resume optimization for internships and entry-level roles
Skill gap analysis for job descriptions
Demonstrating NLP + GenAI system design
Portfolio project for Data Science / AI roles

# Author

Anjali Nevgi
GitHub: https://github.com/Anjalinevgi
