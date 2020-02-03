from django import forms
from .models import Registration
from django.core.validators import RegexValidator
from snowpenguin.django.recaptcha3.fields import ReCaptchaField
from account.models import User
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from datetime import datetime,date

SIG_CHOICES = (
    ('Catalyst','Catalyst'),
    ('Chronicle','Chronicle'),
    ('Clutch', 'Clutch'),
    ('Create','Create'),
    ('Credit','Credit'),
    ('Concrete','Concrete'),
    ('Charge','Charge'),
    ('Crypt','Crypt'),
    ('Club','Club')
    )
members_choices = (
    ('0','0'),
    ('1',1),
    ('3',3),
    ('4',4),
)

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
    section = forms.CharField(label="Section",max_length=50,required=False)
    
class OneForm(forms.Form):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,12}$', message="Phone number invalid")
    # team_name = forms.CharField(label="Team Name",max_length=50,initial="",required=False)
    participant1 = forms.CharField(label="Participant 1",max_length=50,required=True)
    phone1 = forms.CharField(validators=[phone_regex], max_length=17, required=True)
    email = forms.EmailField(required=True)

class EventForm(forms.Form):
    event_name = forms.CharField(label="Event Name",max_length=200,required=True)
    contact1 = forms.ModelChoiceField(queryset=User.objects.all().order_by('first_name','last_name'),required=True)
    contact2 = forms.ModelChoiceField(queryset=User.objects.all().order_by('first_name','last_name'),required=True)
    venue = forms.CharField(label="Venue",max_length=200,required=True)
    description = forms.CharField(widget=CKEditorUploadingWidget(),required=True)
    event_date = forms.DateField(required=True,widget=forms.SelectDateWidget,initial=date.today)
    event_time = forms.TimeField(required=True,widget=forms.TimeInput,initial=datetime.time(datetime.now()))
    sig = forms.ChoiceField(choices=SIG_CHOICES, required=True)
    members=forms.ChoiceField(required=True,choices=members_choices)
    poster_image=forms.FileField()
