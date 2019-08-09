import importlib,os
import django
os.environ['DJANGO_SETTINGS_MODULE'] = 'website.settings'
django.setup()
from recruitments import models as rm
from account import models as am
from django.contrib.auth.models import Group
from django.core.files.images import ImageFile
for s in am.SIG.objects.all():
	for m in rm.ApplicantProgress.objects.filter(sig=am.SIG.objects.get(name=str(s))):
		if m.qualified_for_next:
			l.append([str(m.applicant),str(m.applicant.phone),str(m.applicant.email),str(m.applicant.year)])
	s=SpreadsheetHandler()
	s.excel_write(l,'applicants.xlsx',str(s))