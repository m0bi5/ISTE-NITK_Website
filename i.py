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
from datetime import timedelta

Today= datetime.datetime(year=2019,month=8,day=15,hour=14,minute=0,second=0)
date_list = [Today + datetime.timedelta(minutes=15*x) for x in range(0, 100)]

for s in am.SIG.objects.all():
    if 'Crypt' in str(s):
    
        applicants=SpreadsheetHandler().excel_read('redit.xlsx',str(s))[1:]
        i=0
        a=list(rm.ApplicantProgress.objects.filter(round_completed=2,sig=s))
        for applicant in a:
            applicant.next_round_time=date_list[a.index(applicant)]
            applicant.save()

