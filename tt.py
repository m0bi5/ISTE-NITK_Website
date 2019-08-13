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
    if 'Crypt' in str(s):
        responses=rm.InterviewResponse.objects.filter(sig_round__sig=s)
        for i in range(0,len(responses)):
            if '15' in str(responses[i].criteria):
                print(responses[i].response,responses[i].applicant,responses[i].interviewer)
                c+=1
                try:
                    scores.append(int(responses[i].response))
                except:
                    continue
print(c,' total inteviews')
print(sum(scores)/len(scores),' average')
scoredict={}
k=set(scores)
for i in k:
    scoredict[i]=0
for i in scores:
    scoredict[i]+=1
print(scoredict)
    
