from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'messages']
        widgets = {
            'name':forms.TextInput(attrs={'placeholder': "Write your name..."}),
            'email':forms.TextInput(attrs={'placeholder': "Write your email..."}),
            'message':forms.TextInput(attrs={'placeholder': "Write your message..."}),
        }