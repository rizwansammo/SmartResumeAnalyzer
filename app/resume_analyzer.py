import PyPDF2
import spacy

nlp = spacy.load('en_core_web_sm')

def analyze_resume(file):
    reader = PyPDF2.PdfReader(file)
    text = ''
    for page in reader.pages:
        text += page.extract_text()
    doc = nlp(text)
    skills = [ent.text for ent in doc.ents if ent.label_ == 'SKILL']
    return {"skills": skills}
