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
    if 'Charge' in str(s):
        for applicant in rm.ApplicantProgress.objects.all(sig=s):
            if applicant.next_round_time:
                applicant.round_completed=1
                applicant.save()
            else:
                applicant.round_completed=0
                applicant.qualified_for_next=False
                applicant.save()