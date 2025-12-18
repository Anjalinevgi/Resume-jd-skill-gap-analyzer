 AI-Powered Resume–Job Match & Skill Gap Analyzer

An end-to-end NLP + GenAI application that analyzes how well a resume matches a job description, identifies skill gaps, provides ATS-style feedback, and suggests resume improvements using LLMs.

🔗 GitHub Repository: https://github.com/Anjalinevgi/Resume-jd-skill-gap-analyzer

---

##  Features

- Upload resume (PDF) and paste job description
- Semantic match score using sentence embeddings
- Domain-agnostic skill extraction using Groq LLM
- Rule-based validation to identify missing and implicit skills
- ATS-style heuristic feedback (non-ML, explainable)
- LLM-based resume bullet improvement suggestions
- Interactive Streamlit UI
- Dockerized for reproducibility

---

##  How the System Works

### 1. Semantic Matching
- Resume and Job Description are converted into embeddings using **sentence-transformers**
- **Cosine similarity** is used to compute an overall match score

### 2. Skill Gap Analysis (Hybrid Design)
- Groq LLM suggests relevant skills from the job description
- Suggested skills are **validated**
