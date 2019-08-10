import importlib,os
import django
os.environ['DJANGO_SETTINGS_MODULE'] = 'website.settings'
django.setup()
from recruitments import models as rm
from account import models as am
from django.contrib.auth.models import Group
from django.core.files.images import ImageFile
spots=['181EC202','181EC245','181CV146','16EC142', '181MT029', '181MT003', '181ME156', '181CV113', '181CO130', '181ME162 ', '181ME152', '181ME175', '181EE151', '171IT113', '181ME256', '181CV244', '181ME185', '181EC120', '181EC121', '181ME248', '181EC209', '181IT226', '184CA036', '181CO212', '18EC151', '181EE230', '184CA049', '181CH051', '181EC254', '181CO249', '181EC119', '181IT249', '181EC119', '181IT140', '181EC110', '181EC153', '181ME110', '181ME140', '181IT240', '181ch026', '181IT240', '181ME277', '181ME227', '181ME178', '181ME275', '181CV152', '181MT008', '181EC109', '181MT034', '171EC220', '181CO239', '181MT032', '181EE126', '181ME204', '181CO135', '181CV210', '181IT102', '181EC252', '181CV238', '181EC246 ', '181IT104', '181CO121 ', '181IT221', '18EE253', '17CV249', '181CO108', '18EC125', '181CO152 ', '181EC155', '171ME177']
from helper import *
l=[]
for s in am.SIG.objects.all():
	for m in rm.ApplicantProgress.objects.filter(sig=am.SIG.objects.get(name=str(s))):
		if m.qualified_for_next and m.applicant.rollno in spots:
			l.append([str(m.sig),str(m.applicant),str(m.applicant.phone),str(m.applicant.email),str(m.applicant.year)])
	t=SpreadsheetHandler()
	t.excel_write(l,str(s)+'.xlsx',str(s))
