from django import forms
from .models import Experience

from .models import Education

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['title' , 'company' , 'location', 'start_date', 'end_date', 'description']


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['start_year', 'end_year', 'institution', 'location','degree', 'field_of_study','description']