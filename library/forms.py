from django import forms
from library.models import Library


class LibraryModelForm(forms.ModelForm):
    class Meta:
        model = Library
        fields = '__all__'
