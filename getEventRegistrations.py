import importlib,os
import django
os.environ['DJANGO_SETTINGS_MODULE'] = 'website.settings'
django.setup()
from events.models import *
import xlsxwriter

def excel_write(dataset,file,worksheet_name):
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

def create_event_excel_sheet(event_name):
    event = EventDetails.objects.get(event_name=event_name)
    n = event.members
    reg = []
    if n==1:
        l=['Name','Phone number','Email']
        reg.append(l)
        for obj in OneMember.objects.filter(event=event):
            l = [obj.participant1,obj.phone1,obj.email]
            reg.append(l)
    elif n==3:
        l=['Team Name','Particpant 1','Participant 2','Participant 3',"Contact 1",'Contact 2','Email']
        reg.append(l)
        for obj in ThreeMember.objects.filter(event=event):
            l=[obj.team_name,obj.participant1,obj.participant2,obj.participant3,obj.phone1,obj.phone2,obj.email]
            reg.append(l)
    else:
        l = ['Team Name','Particpant 1','Participant 2','Participant 3','Participant 4',"Contact 1",'Contact 2','Email']
        reg.append(l)
        for obj in FourMember.objects.filter(event=event):
            l=[obj.team_name,obj.participant1,obj.participant2,obj.participant3,obj.participant4,obj.phone1,obj.phone2,obj.email]
            reg.append(l)

    excel_write(reg,event_name+'.xlsx',event_name)
    print("Registrations exported")
