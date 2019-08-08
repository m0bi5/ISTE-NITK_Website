from django import forms
from django.core.validators import RegexValidator
from account import models as account_models
from snowpenguin.django.recaptcha3.fields import ReCaptchaField

year_choices = (
    ('2nd year','2nd year'),
    ('3rd year','3rd year'))

class recaptchaForm(forms.Form):
    recaptcha=ReCaptchaField(score_threshold=0.75)
    


class ApplicantForm(forms.Form):
    rollno_regex = RegexValidator(regex=r'^1[78]1(IT|CV|MN|MT|ME|CS|EE|EC|CH|CO)[012][0-9][0-9]$',message="Roll number must be in the format: 1[7/8]1XX[1/2]XX")
    rollno = forms.CharField(validators=[rollno_regex],label="Roll no",max_length=8,required=True)
    first_name = forms.CharField(label="First name",max_length=50,required=True)
    last_name = forms.CharField(label="Second name",max_length=50,required=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,12}$', message="Phone number invalid")
    phone = forms.CharField(validators=[phone_regex], max_length=17, required=True)
    email = forms.EmailField(required=True)
    year = forms.ChoiceField(choices=year_choices, required=True)
    sigs=account_models.SIG.objects.all()
    captcha=ReCaptchaField(score_threshold=0.25)
    sig_choices = forms.ModelMultipleChoiceField(widget=forms.SelectMultiple(attrs={'data-limit':'3','class':'limit'}),queryset=account_models.SIG.objects.all(),required=True)
