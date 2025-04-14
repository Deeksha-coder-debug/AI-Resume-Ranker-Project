from django.shortcuts import render
# I use render() to return form and results to frontend.
from .forms import ResumeForm
# Importing the form class.This brings in our form with resume & JD fields.
from .utils import extract_text_from_resume, calculate_match_score
# I modularized resume parsing and scoring in a utility file to keep views clean

def index(request):
    # function controls what happens on form load and submission.
    if request.method == 'POST':
    # Checks if form was submitted	“POST means the user submitted data via form.”
        form = ResumeForm(request.POST, request.FILES)
        # Loads submitted form data	“Includes both text and uploaded files.”

        if form.is_valid():
        # Validates form input	“Ensures required fields are filled and types are correct.” 
            resume = form.cleaned_data['resume_file']
            # use cleaned_data to safely extract validated inputs.
            jd_text = form.cleaned_data['job_description']
            # Same for the job description.
            resume_text = extract_text_from_resume(resume)
            # Parse resume into text	“This reads the resume (PDF/DOCX) into raw text for processing.”

            score, feedback = calculate_match_score(resume_text, jd_text)
            # AI matching logic	“Compares resume text with JD using a keyword scoring algorithm.”

            return render(request, 'ranker/result.html', {
                'score': score,
                'feedback': feedback
            })
            # Show result	“Passes score and feedback to the result page.”
    else:
        form = ResumeForm()
        # On GET request	“If not POST, it’s the first visit, so just show the form.”

    return render(request, 'ranker/index.html', {'form': form})
    # Load form page	“Loads the form into the homepage.”

# Create your views here.
