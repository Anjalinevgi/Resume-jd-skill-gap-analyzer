def ats_feedback(resume_text):
    feedback = []

    if len(resume_text.split()) < 350:
        feedback.append("Resume may be too short for ATS parsing.")

    if "%" not in resume_text:
        feedback.append("Add quantifiable metrics (%, numbers).")

    if resume_text.count("•") < 5:
        feedback.append("Bullet structure could be improved.")

    return feedback
