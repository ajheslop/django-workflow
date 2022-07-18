from django.forms import ModelForm, widgets
from .models import Project
from django import forms
# model form requires 2 fields ()


class ProjectForm(ModelForm):
    class Meta:
        model = Project #1st requirement for the project name you're doing it for in models
        fields = ['title','featured_image','description','demo_link', 'source_link', 'tags' ]   #2nd requirement
        widgets = {
                'tags':forms.CheckboxSelectMultiple(),
            }
        
        
        def __init__(self, *args, **kwargs):
            super(ProjectForm, self).__init__(*args, **kwargs)
            
            self.fields['title'].widget.attrs.update({'class':'input', 'placeholder':'Add Title'})