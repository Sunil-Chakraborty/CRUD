# forms.py

from django import forms
from .models import Directory, File

class DirectoryForm(forms.ModelForm):
    class Meta:
        model = Directory
        fields = ['name', 'parent']

class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['name', 'file', 'directory']
