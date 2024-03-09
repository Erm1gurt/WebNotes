from django import forms
from .models import Notes


class CreateNote(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['note_text']

        labels = {
            'note_text': 'Заметка',
        }

        widgets = {
            'note_text': forms.TextInput(attrs={'name': 'note-text'})
        }