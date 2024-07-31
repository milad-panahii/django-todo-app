from django import forms
from .models import Todo

class TodoCreateForms(forms.form):
    title=forms.CharField()
    body=forms.CharField()
    created=forms.DateTimeField()
    
    
class TodoUpdateForms(forms.ModelForm):
    class meta:
        model = Todo
        fields = ('title', 'body', 'created')