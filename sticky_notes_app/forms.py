# Import forms module
from django import forms

# Import note model
from .models import Note


# Define class for form
class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ["title", "content"]
