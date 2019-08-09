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
    applicants=SpreadsheetHandler().excel_read('slots.xlsx',str(s))[1:]
    i=0
    for applicant in applicants:
        applicant[1]=str(int(applicant[1]))
        m=rm.ApplicantProgress.objects.get(applicant=rm.Applicant.objects.get(phone=applicant[1]),sig=s)
        m.next_round_location=applicant[-1]
        date_time_str=applicant[-3]+' '+applicant[-2]
        date=datetime.datetime.strptime(date_time_str, '%d/%m/%Y %H:%M:%S')
        m.next_round_time=date
        m.save()
        EmailHandler().send_email(m.applicant.email,'An update on your application!','Hello '+m.applicant.first_name+'\n An update on your applicant status has been made, you may check your progress here: http://iste.nitk.ac.in/recruitments/progress/'+m.applicant.rollno,'istenitkchapter@gmail.com','tqlsyhqfyskwutxh')
        i+=1
        print(str(s),': ',i,' out of ',len(applicants), 'done')