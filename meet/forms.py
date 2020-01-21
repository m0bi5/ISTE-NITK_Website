from django import forms
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




class MeetForm(forms.Form):
    topic = forms.CharField(widget=CKEditorUploadingWidget(),required=True)
    date = forms.DateField(required=True,widget=forms.SelectDateWidget,initial=date.today)
    start_time = forms.TimeField(required=True,widget=forms.TimeInput,initial=datetime.time(datetime.now()))
    end_time = forms.TimeField(required=True,widget=forms.TimeInput,initial=datetime.time(datetime.now()))
    sig = forms.ChoiceField(choices=SIG_CHOICES, required=True)
    venue = forms.CharField(label="Venue",max_length=200,required=True,initial="ISTE Office")
