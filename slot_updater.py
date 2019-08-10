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


for s in am.SIG.objects.all():
    if 'Crypt' in str(s) or 'Catalyst' in str(s):
        continue
    applicants=SpreadsheetHandler().excel_read('slots.xlsx',str(s))[1:]
    i=0
    for applicant in applicants:
        try:
            applicant[1]=str(int(applicant[1]))
            m=rm.ApplicantProgress.objects.get(applicant=rm.Applicant.objects.get(phone=applicant[1]),sig=s)
            m.next_round_location=applicant[-1]
            date_time_str=str(applicant[-3])+' '+str(applicant[-2])
            try:
                date=datetime.datetime.strptime(date_time_str, '%d/%m/%Y %H:%M:%S')
            except:
                date=datetime.datetime.strptime(date_time_str+':00', '%d/%m/%Y %H:%M:%S') 
            m.next_round_time=date
            m.save()
            i+=1
            print(str(s),': ',i,' out of ',len(applicants), 'done')
        except:
            FileHandler().text_write([applicant[1]],applicant[1]+'.txt')

