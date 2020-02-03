import json
import urllib

import smtplib,ssl
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import formatdate
from email import encoders
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages
from .forms import *
from .models import *
from .emailer import EmailHandler as em
from django.urls import reverse
from getEventRegistrations import create_event_excel_sheet as exsheet
# Create your views here.
def event_view(request):
    all_events=EventDetails.objects.all()
    context={
        'all_events':all_events
    }
    return render(request, "events/event_view.html",context)

def event_form_team(request,event_id,roll_no):
    event=EventDetails.objects.get(id=event_id)
    if request.POST:
        if request.POST['member2'] or request.POST['member3']:
            if Registration.objects.filter(event=event,roll_no=request.POST['member2']).first() or Registration.objects.filter(event=event,roll_no=request.POST['member3']).first():
                team=Team.objects.create(event=event,team_name=request.POST['team_name'],member1=roll_no,member2=request.POST['member2'],member3=request.POST['member3'])
                team.save()
                messages.success(request,"Team successfully created!")
            else:
                messages.error(request,"Ask your team mates to register for the event first!")
        else:
            team=Team.objects.create(event=event,team_name=request.POST['member1'],member1=roll_no)
            team.save()
            messages.success(request,"Team successfully created!")

    return render(request, "events/event_teams.html",{'member1':roll_no,'form':TeamForm(),'event':event})



def event_register(request, event_id):
    event=EventDetails.objects.get(id=event_id)
    if request.method == 'POST':
        form = None
        if event.members==3:
            form=ThreeForm(request.POST)
        if event.members==1:
            form=OneForm(request.POST)
        if event.members==4:
            form=FourForm(request.POST)
        if form.is_valid():
            obj=None
            add = None
            if event.members==3:
                add = request.POST['team_name']
                obj=ThreeMember(event=event,team_name=request.POST['team_name'],participant1=request.POST['participant1'],participant2=request.POST['participant2'],participant3=request.POST['participant3'],phone1=request.POST['phone1'],phone2=request.POST['phone2'],email=request.POST['email'])                
            elif event.members==4:
                add = request.POST['team_name']
                obj=FourMember(event=event,team_name=request.POST['team_name'],participant1=request.POST['participant1'],participant2=request.POST['participant2'],participant3=request.POST['participant3'],participant4=request.POST['participant4'],phone1=request.POST['phone1'],phone2=request.POST['phone2'],email=request.POST['email'])
            elif event.members==1:
                add = request.POST['participant1']
                obj=OneMember(event=event,  participant1=request.POST['participant1'],phone1=request.POST['phone1'],email=request.POST['email'])
            obj.save()
            em_obj=em()
            em_obj.send_email(request.POST['email'],"You have registered for ISTE NITK's "+event.event_name,"Hello "+add+"!\n\nThank you for registering for "+event.event_name+"! The event will be held on "+str(event.event_date)+" at "+event.venue+".\nWe look forward to seeing you there!\n\nWith love,\nISTE NITK",'istenitkchapter@gmail.com','#includeistenitk.h')
            messages.success(request, 'Thank you for registering!')
        else:
            print(form.errors)
            messages.error(request, 'Invalid details entered! Please try again.')
            return redirect(event_register,event_id)
    else:
        if event.members==3:
            form=ThreeForm()
        if event.members==1:
            form=OneForm()
        if event.members==4:
            form = FourForm()
    context = {
        'form': form,
        'four': event.members==4,
        'one' : event.members==1,
        'zero' : event.members==3   #Spectacle jugaad fixup plss
    }
    return render(request,"events/event_registration.html", context)

@login_required(login_url='/account/login')
def view_registrations(request,event_id):
    event = EventDetails.objects.get(id=event_id)
    regs = []
    one = False
    four= False
    if event.members==1:
        objs = OneMember.objects.filter(event=event)
        one = True
        for obj in objs:
            l=[obj.participant1,obj.phone1,obj.email]
            regs.append(l)
    elif event.members==3:
        objs = ThreeMember.objects.filter(event=event)
        for obj in objs:
            l = [obj.team_name,obj.participant1,obj.participant2,obj.participant3,obj.phone1,obj.phone2,obj.email]
            regs.append(l)
    elif event.members==4:
        objs = ThreeMember.objects.filter(event=event)
        four = True
        for obj in objs:
            l = [obj.team_name,obj.participant1,obj.participant2,obj.participant3,obj.participant4,obj.phone1,obj.phone2,obj.email]
            regs.append(l)

    if request.method=='GET':
        return render(request,'events/view_registrations.html',{'one':one,'four':four,'regs':regs,'event_name':event.event_name})
    else:
        exsheet(event.event_name)
        file = event.event_name+'.xlsx'
        username='istenitkchapter@gmail.com'
        password='#includeistenitk.h'
        send_from = username
        send_to = request.user.email

        msg = MIMEMultipart()
        msg['From'] = send_from
        msg['To'] = send_to
        msg['Subject'] = 'Registrations for '+event.event_name
        server = smtplib.SMTP('smtp.gmail.com',587)
        fp = open(file, 'rb')
        part = MIMEBase('application','vnd.ms-excel')
        part.set_payload(fp.read())
        fp.close()
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment', filename=file)
        msg.attach(part)
        smtp = smtplib.SMTP('smtp.gmail.com',587)
        smtp.ehlo()
        smtp.starttls()
        smtp.login(username,password)
        smtp.sendmail(send_from, send_to, msg.as_string())
        smtp.quit()
        print("Mail sent successfully")
        messages.success(request,"Event registration details mailed to "+send_to)
        return render(request,'events/view_registrations.html',{'one':one,'four':four,'regs':regs,'event_name':event.event_name})

def handle_uploaded_file(f):
     with open('media/'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

@login_required(login_url='/account/login')
def create_event(request):
    if request.method=='GET':
        if request.user.groups.filter(name='Core').exists():
            form = EventForm()
            return render(request,'events/create_event.html',{'form':form})
        else:
            messages.error(request,'Only ISTE Core members can access this page!')
            return redirect('/events/')
    else:
        form = EventForm(request.POST,request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['poster_image'])
            event = EventDetails(event_name=request.POST['event_name'],contact1=User.objects.get(id=int(request.POST['contact1'])),contact2=User.objects.get(id=int(request.POST['contact2'])),
                    venue=request.POST['venue'],description=request.POST['description'],event_date=request.POST['event_date_year']+'-'+request.POST['event_date_month']+'-'+request.POST['event_date_day'],event_time=request.POST['event_time'],
                    sig=request.POST['sig'],members=request.POST['members'],poster_image=request.POST['poster_image'])
            event.save()
            messages.success(request,'New event '+request.POST['event_name']+' created successfully!')
            return render(request,'events/create_event.html',{'form':form})
        messages.error(request,'Invalid input(s)! Please check again!')
        return render(request,'events/create_event.html',{'form':form})

