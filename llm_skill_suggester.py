import os
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def suggest_skills_from_jd(jd_text):
    prompt = f"""
Extract a concise list of skills explicitly or implicitly required from the job description below.

Rules:
- Return ONLY a comma-separated list
- Do NOT explain anything
- Do NOT add irrelevant or senior-only skills
- Focus on skills a candidate would be evaluated on

Job Description:
{jd_text}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    skills_text = response.choices[0].message.content
    skills = [s.strip().lower() for s in skills_text.split(",") if s.strip()]
    return skills
