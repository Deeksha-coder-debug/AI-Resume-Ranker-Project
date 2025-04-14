from django import forms

class ResumeForm(forms.Form):
    resume_file = forms.FileField(label="Upload Your Resume")
    job_description = forms.CharField(
        label="Paste Job Description",
        widget=forms.Textarea(attrs={'placeholder': 'Paste the job description here...', 'rows': 5})
    )

