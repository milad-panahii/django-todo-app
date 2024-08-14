from django import forms
from .models import Todo

class TodoCreateForms(forms.Form):
    title=forms.CharField()
    body=forms.CharField()
    created=forms.DateTimeField()
    
    
class TodoUpdateForms(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('title', 'body', 'created')
        
        # widgets = {
        #     'created':forms.TextInput(attrs={'type':'datetime-local'}),
        # }