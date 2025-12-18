from groq import Groq
import os

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def improve_bullet(bullet, jd_context):
    prompt = f"""
Rewrite this resume bullet to better match the job description.
Do NOT add fake experience.

Bullet: {bullet}
Job Description: {jd_context}
"""
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )
    return response.choices[0].message.content

'''
Low temperature

No hallucinated experience

LLM used as language assistant, not decision-maker
'''