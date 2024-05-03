# forms.py
from django import forms
from .models import ConverterUploadedFile

class UploadedFileForm(forms.ModelForm):
    class Meta:
        model = ConverterUploadedFile
        fields = ['file']
