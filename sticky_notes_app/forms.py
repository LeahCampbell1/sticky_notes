
# Import forms module
from django import forms

# Import note model
from .models import Note


class NoteForm(forms.ModelForm):
    """Provide a form for creating and updating notes.

    Uses the Note model to generate form fields.
    """

    class Meta:
        """Configure the NoteForm model and fields.

        :param model: The model associated with the form.
        :type model: Note
        :param fields: The model fields included in the form.
        :type fields: list
        """

        model = Note
        fields = ["title", "content"]
