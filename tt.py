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
a=SpreadsheetHandler().excel_read('Book1.xlsx')
l=[str(int(i[0])) for i in a]
print(l)
for s in am.SIG.objects.all():
    if 'Chronicle' in str(s):
        for a in rm.ApplicantProgress.objects.filter(sig=s):
            #responses=rm.InterviewResponse.objects.filter(sig_round__sig=s,applicant=a.applicant)
            if a.applicant.phone in l:
                
                print(a.applicant.first_name,a.applicant.phone)
                a.qualify()
            else:
                a.disqualify()

            '''
            if len(responses)>0:
                print(a.applicant,len(responses))
                d={'Name':a.applicant.first_name+' '+a.applicant.last_name,'Technical Knowledge':0,'Communication Skills':0,'Problem Solving':0,'Conduct':0}
                for i in range(0,len(responses)):
                    cri=responses[i].criteria.body.split('>')[1].split('<')[0]
                    if cri in ['Technical Knowledge','Communication Skills','Problem Solving','Conduct']:
                        d[cri]=responses[i].response
                scores.append(d)

            '''
'''
a=[]
for i in scores:
    a.append(list(i.values()))
print(len(a))
t=SpreadsheetHandler()
t.excel_write(a,'Charge interviews'+'.xlsx','Sheet1')
'''