import importlib,os
import django
os.environ['DJANGO_SETTINGS_MODULE'] = 'website.settings'
django.setup()
from account import models
from django.contrib.auth.models import Group
from django.core.files.images import ImageFile
from helper import *

sheet=SpreadsheetHandler()
sigs=['Crypt','Charge','Chronicle','Clutch','Concrete','Create','Credit','Catalyst']
l=sheet.excel_read('list.xlsx','2nd Years')[1:]
accounts=[]
for members in l:
    name=members[0]
    email=members[-1]
    username="".join(name.split(' '))
    username=username.lower()
    first_name=name.split(' ')[0]
    last_name=name.replace(first_name,"")
    sig_models=list(models.SIG.objects.all())
    sig_responses=members[1:-1]
    my_sigs=[]
    for i in range(len(sig_responses)):
        if 'Y' in sig_responses[i] or 'y' in sig_responses[i]:
            for sig_model in sig_models:
                if sig_model.name.lower()==sigs[i].lower():
                    my_sigs.append(sig_model)
    try:
        if len(my_sigs)!=0:
            u=models.User.objects.create(username=username,first_name=first_name,last_name=last_name,email=email,batch_of=2020)
            u.is_staff=True
            u.sigs.set(my_sigs)
            u.groups.add(Group.objects.get(name='Member'))
            u.set_password('istenitk')
            u.avatar=ImageFile(open("media/generic_pp.jpg", "rb"))
            u.save()
    except Exception as e:
        print(e)
        print(username," already exists")
