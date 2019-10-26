from django import forms
from .models import Registration
from django.core.validators import RegexValidator
from snowpenguin.django.recaptcha3.fields import ReCaptchaField


class FourForm(forms.Form):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,12}$', message="Phone number invalid")
    team_name = forms.CharField(label="Team Name",max_length=50,required=True)
    participant1 = forms.CharField(label="Participant 1",max_length=50,required=True)
    participant2 = forms.CharField(label="Participant 2",max_length=50,required=True)
    participant3 = forms.CharField(label="Participant 3",max_length=50,required=True)
    participant4 = forms.CharField(label="Participant 4 (Optional)",max_length=50,required=False)
    phone1 = forms.CharField(validators=[phone_regex], max_length=17, required=True)
    phone2 = forms.CharField(validators=[phone_regex], max_length=17, required=True)
    email = forms.EmailField(required=True)

class ThreeForm(forms.Form):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,12}$', message="Phone number invalid")
    team_name = forms.CharField(label="Team Name",max_length=50,required=True)
    participant1 = forms.CharField(label="Participant 1",max_length=50,required=True)
    participant2 = forms.CharField(label="Participant 2",max_length=50,required=True)
    participant3 = forms.CharField(label="Participant 3 (Optional)",max_length=50,required=False)
    phone1 = forms.CharField(validators=[phone_regex], max_length=17, required=True)
    phone2 = forms.CharField(validators=[phone_regex], max_length=17, required=True)
    email = forms.EmailField(required=True)    
    
class OneForm(forms.Form):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,12}$', message="Phone number invalid")
    team_name = forms.CharField(label="Team Name",max_length=50)
    participant1 = forms.CharField(label="Participant 1",max_length=50,required=True)
    phone1 = forms.CharField(validators=[phone_regex], max_length=17, required=True)
    email = forms.EmailField(required=True)  
