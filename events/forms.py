from django import forms
from .models import Registration


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = [
            'first_name',
            'last_name',
            'roll_no',
            'email',
            'contact_number'
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'first name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'last name'}),
            'roll_no': forms.TextInput(attrs={'placeholder': 'roll no'}),
            'email': forms.EmailInput(attrs={'placeholder': 'email'}),
            'contact_number': forms.TextInput(attrs={'placeholder': 'contact number'}),

        }
