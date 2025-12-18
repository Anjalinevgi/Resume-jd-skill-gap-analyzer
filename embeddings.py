from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")

def compute_match_score(resume_text, jd_text):
    embeddings = model.encode([resume_text, jd_text])
    score = cosine_similarity([embeddings[0]], [embeddings[1]])[0][0]
    return round(score * 100, 2)

def split_sections(text):
    sections = {
        "skills": "",
        "experience": "",
        "education": ""
    }

    for key in sections:
        if key in text:
            sections[key] = text.split(key)[1][:500]

    return sections
