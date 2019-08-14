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
scores=[]
c=0
for s in am.SIG.objects.all():
    if 'Credit' in str(s):
        for a in rm.ApplicantProgress.objects.filter(sig=s):
            responses=rm.InterviewResponse.objects.filter(sig_round__sig=s,applicant=a.applicant)
            if len(responses)>0:
                d={'Name':a.applicant.first_name+' '+a.applicant.last_name,'domain specific knowledge':0,'guestimate':0,'something unusal and extraordinary':0,'total score out of 20':0,'How fit is the candidate for':0}
                for i in range(0,len(responses)):
              
                    for j in ['domain specific knowledge','guestimate','something unusal and extraordinary','total score out of 20','How fit is the candidate for']:
                    	if j in responses[i].criteria.body:
                    		d[j]=responses[i].response
                    		print('111')
                scores.append(d)
a=[]
for i in scores:
    a.append(list(i.values()))
print(len(a))
t=SpreadsheetHandler()
t.excel_write(a,'Credit interviews'+'.xlsx','Sheet1')