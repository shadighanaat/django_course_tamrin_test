from django import forms
from .models import Members


class NewMembersForm(forms.ModelForm):
    class Meta:
        model = Members
        fields = ['title', 'text', 'author', 'status']
