from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'phone', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Your Name'}),
            'phone': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Your Phone'}),
            'email': forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'Your Email'}),
            'message': forms.Textarea(attrs={'class': 'form-textarea', 'rows': 4, 'placeholder': 'Your Message'}),
        }
