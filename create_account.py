import importlib,os
import django
os.environ['DJANGO_SETTINGS_MODULE'] = 'website.settings'
django.setup()
from account import models
from django.contrib.auth.models import Group
from django.core.files.images import ImageFile
import xlrd,xlsxwriter

def excel_read(file,sheet_name='Sheet1'):  
        book = xlrd.open_workbook(file)
        sheet = book.sheet_by_name(sheet_name)
        data = [[sheet.cell_value(r, c) for c in range(sheet.ncols)] for r in range(sheet.nrows)]
        return data

def excel_write(dataset,file,worksheet_name="Usernames"):
        workbook = xlsxwriter.Workbook(file)
        worksheet = workbook.add_worksheet(worksheet_name)
        n=1
        for data in dataset:
            c='A'
            for x in data:
                cell=c+str(n)
                worksheet.write(cell, x)
                c=chr(ord(c)+1)
            n+=1
        workbook.close()

l=excel_read('ISTEJuniors.xlsx','juniors')[1:]
accounts=['Name','Username']
for members in l:
    email=members[0].strip()

    first_name=members[1]
    
    last_name=members[2]

    name=first_name+last_name
    username="".join(name.split(' '))
    username=username.lower()
    accounts.append([first_name+" "+last_name,username])
    
    pno = str(int(members[4]))
    
    sig_models=list(models.SIG.objects.all())
    sigs = {}
    for sg in sig_models:
        sigs[sg.name.lower()] = sg
    sig_responses=members[3].split(',')
    my_sigs=[]

    for sig in sig_responses:
        my_sigs.append(sigs[sig.strip()])
    try:
        if len(my_sigs)!=0:
            u=models.User.objects.create(username=username,first_name=first_name,last_name=last_name,email=email,batch_of=2022,phone_number=pno)
            u.is_staff=True
            u.sigs.set(my_sigs)
            u.groups.add(Group.objects.get(name='Member'))
            u.set_password('istenitk')
            u.avatar=ImageFile(open("media/user_10/avatar/generic_pp.jpg", "rb"))
            u.save()
    except Exception as e:
        print(e)
        print(username," already exists")

excel_write(accounts,'JunoirsUsernames.xlsx')
print("Done")
