import pdfplumber
import re

def extract_resume_text(pdf_file):
    text = ""
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"

    # basic cleaning
    text = re.sub(r'\s+', ' ', text)
    return text.lower()
