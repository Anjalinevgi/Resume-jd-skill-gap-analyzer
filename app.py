import streamlit as st

from resume_parser import extract_resume_text
from embeddings import compute_match_score
from llm_feedback import improve_bullets

from llm_skill_suggester import suggest_skills_from_jd
from skill_gap import skill_gap, SKILL_SYNONYMS
from ats_rules import ats_feedback


st.title("AI Resume–Job Match & Skill Gap Analyzer")

resume_file = st.file_uploader("Upload Resume (PDF)")
jd_text = st.text_area("Paste Job Description")


if resume_file and jd_text:
    # 1. Extract resume text
    resume_text = extract_resume_text(resume_file)

    # 2. Compute semantic match score (embeddings)
    score = compute_match_score(resume_text, jd_text)

    # 3. Use Groq to suggest skills from JD
    llm_skills = suggest_skills_from_jd(jd_text)

    # 4. Validate skills against resume (rules + synonyms)
    missing, matched = skill_gap(
        resume_text,
        jd_text,
        llm_skills,
        SKILL_SYNONYMS
    )

    # 5. ATS heuristic feedback
    ats_issues = ats_feedback(resume_text)

    # ---------------- DISPLAY ---------------- #

    st.metric("Match Score", f"{score}%")

    st.subheader("Suggested Skills from Job Description")
    st.write(llm_skills)

    st.subheader("Missing Skills")
    st.write(missing if missing else "No critical missing skills found")

    st.subheader("Matched / Implicit Skills")
    st.write(matched)

    st.subheader("ATS Heuristic Feedback")
    if ats_issues:
        for issue in ats_issues:
            st.warning(issue)
    else:
        st.success("No major ATS formatting issues detected.")

    # 6. LLM-based resume improvement
    if st.button("Improve Resume Bullets"):
        feedback = improve_bullets(resume_text, jd_text)
        st.text_area("LLM Suggestions", feedback, height=300)
