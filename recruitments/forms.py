from django import forms
from django.core.validators import RegexValidator

year_choices = (
    ('2nd year','2nd year'),
    ('3rd year','3rd year'))

sig_choices=(
    ('Crypt','CRYPT'),
    ('Charge','CHARGE'),
    ('Credit','CREDIT'),
    ('Chronicle','CHRONICLE'),
    ('Clutch','CLUTCH'),
    ('Concrete','CONCRETE'),
    ('Create','CREATE'),
    ('Catalyst','CATALYST'))

class ApplicantForm(forms.Form):
    rollno_regex = RegexValidator(regex=r'^1[78]1\b(IT|MN|MT|ME|CS|EE|EC|CH)\b[12][0-7][0-9]$',message="Roll number must be in the format: 181IT107")
    rollno = forms.CharField(label="Roll no",max_length=8,required=True)
    first_name = forms.CharField(label="First name",max_length=50,required=True)
    last_name = forms.CharField(label="Second name",max_length=50,required=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = forms.CharField(validators=[phone_regex], max_length=17, required=True)
    email = forms.EmailField(required=True)
    year = forms.ChoiceField(choices=year_choices, required=True)
    sig_choices = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices = sig_choices,required=True)
