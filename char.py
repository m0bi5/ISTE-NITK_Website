import importlib,os
import django
os.environ['DJANGO_SETTINGS_MODULE'] = 'website.settings'
django.setup()
from recruitments import models as rm
from account import models as am
from django.contrib.auth.models import Group
from django.core.files.images import ImageFile
from helper import *
import datetime

qualified_numbers=[]

for s in am.SIG.objects.all():
    applicants=SpreadsheetHandler().excel_read('slots.xlsx',str(s))[1:]
    for applicant in applicants:
    	rm.ApplicantProgress.objects.get(sig=s,applicant=rm.Applicant.objects.get(phone=applicant[1]))

for s in am.SIG.objects.all():
    if 'Charge' in str(s):
        applicants=rm.ApplicantProgress.objects.filter(sig=s)
        for applicant in applicants:
        	if applicant.applicant.phone in qualified_numbers:
        		applicant.qualify()
        	else:
        		applicant.disqualify()

print(qualified_numbers)