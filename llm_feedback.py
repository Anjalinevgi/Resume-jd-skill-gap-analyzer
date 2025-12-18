from groq import Groq
import os

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def improve_bullets(resume_text, jd_text):
    prompt = f"""
You are an ATS resume expert.
Improve the resume bullets to better match the job description.
Do not fabricate experience.

Resume:
{resume_text}

Job Description:
{jd_text}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
