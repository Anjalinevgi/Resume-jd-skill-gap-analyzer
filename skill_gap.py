
SKILL_SYNONYMS = {
    "machine learning": [
        "ml",
        "classification",
        "regression",
        "ensemble",
        "random forest",
        "xgboost",
        "svm",
        "scikit-learn"
    ],
    "deep learning": [
        "dl",
        "cnn",
        "rnn",
        "lstm",
        "transformer",
        "bert",
        "neural network",
        "pytorch",
        "tensorflow"
    ],
    "nlp": [
        "natural language processing",
        "text processing",
        "sentiment analysis",
        "transformers",
        "bert",
        "gpt"
    ]
}


SKILLS = [
    "python", "sql", "machine learning", "deep learning",
    "nlp", "pandas", "numpy", "tensorflow", "pytorch",
    "data visualization", "statistics"
]

def skill_present(skill, resume_text, synonym_map):
    resume_text = resume_text.lower()

    if skill in resume_text:
        return True

    if skill in synonym_map:
        for syn in synonym_map[skill]:
            if syn in resume_text:
                return True

    return False


def normalize_text(text):
    return text.lower()


def extract_skills(text):
    text = normalize_text(text)
    found_skills = set()

    # Direct skill matches
    for skill in SKILLS:
        if skill in text:
            found_skills.add(skill)

    # Synonym-based matches
    for canonical_skill, synonyms in SKILL_SYNONYMS.items():
        for syn in synonyms:
            if syn in text:
                found_skills.add(canonical_skill)
                break

    return found_skills


def skill_gap(resume_text, jd_text, llm_skills, synonym_map):
    resume_text = resume_text.lower()

    confirmed = []
    weak = []
    missing = []

    for skill in llm_skills:
        if skill_present(skill, resume_text, synonym_map):
            confirmed.append(skill)
        else:
            missing.append(skill)

    return missing, confirmed


