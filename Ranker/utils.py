import docx2txt    # For reading .docx
import PyPDF2    # For reading .docx
# “I used lightweight parsers for extracting resume text—fast and reliable.

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
#  TF-IDF & cosine similarity
#  For comparing resume & JD, I used 
# vectorization + cosine similarity, a common NLP technique.

def extract_text_from_resume(resume_file):
# Text extraction function	
# Handles both PDF and DOCX parsing in a single reusable function.
    if resume_file.name.endswith('.pdf'):
    # File type detection	“Basic validation for supported file types.”
        pdf_reader = PyPDF2.PdfReader(resume_file)
        # Read PDF content and stores it in variable
        # “Iterates through each page and extracts text using PyPDF2.”
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text() or ""
        return text
    elif resume_file.name.endswith('.docx'):
        return docx2txt.process(resume_file)
        # Read DOCX content	“Returns clean raw text from Word files.”
    else:
        return ""

def calculate_match_score(resume_text, job_description):
    vectorizer = TfidfVectorizer(stop_words='english')
    # NLP step 1: tokenize	
    # “Converts both resume and JD into TF-IDF vectors, ignoring stop words.”
    tfidf = vectorizer.fit_transform([resume_text, job_description])
    score = cosine_similarity(tfidf[0:1], tfidf[1:2])[0][0]
    # NLP step 2: compare	
    # “Compares two vectors to find similarity score (1 = identical, 0 = unrelated).”
    feedback = generate_feedback(score)
    return round(score * 100, 2), feedback
    # Make it a percentage	
    # “I round it to a clean match score (like 84.56%) for user-friendly output.”

def generate_feedback(score):
# Returns advice based on the score
    if score > 0.8:
        return "🚀 Excellent match! Your resume aligns very well with the job description."
    elif score > 0.5:
        return "👍 Good match. Consider adding more role-specific keywords."
    else:
        return "⚠️ Low match. You might need to tailor your resume more to the job."
