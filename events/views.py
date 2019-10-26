import json
import urllib

from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages
from .forms import *
from .models import *
from .emailer import EmailHandler as em
from django.urls import reverse

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
            if event.members==3:
                obj=ThreeMember(event=event,team_name=request.POST['team_name'],participant1=request.POST['participant1'],participant2=request.POST['participant2'],participant3=request.POST['participant3'],phone1=request.POST['phone1'],phone2=request.POST['phone2'],email=request.POST['email'])
            if event.members==4:
                obj=FourMember(event=event,team_name=request.POST['team_name'],participant1=request.POST['participant1'],participant2=request.POST['participant2'],participant3=request.POST['participant3'],participant4=request.POST['participant4'],phone1=request.POST['phone1'],phone2=request.POST['phone2'],email=request.POST['email'])       
            if event.members==1:
                obj=OneMember(event=event,team_name=request.POST['participant1'],participant1=request.POST['participant1'],phone1=request.POST['phone1'],email=request.POST['email']) 
            obj.save()
            em_obj=em()
           # em_obj.send_email(request.POST['email'],"You have registered for ISTE NITK's "+event.event_name,"Hello "+request.POST['participant1']+"!\n Thank you for registering for "+event.event_name+" which will be held on "+str(event.event_date),'istenitkchapter@gmail.com','tqlsyhqfyskwutxh')
            messages.success(request, 'Thank you for registering!')
        else:
            print(form.errors)
            messages.error(request, 'Invalid reCAPTCHA. Please try again.')

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
        'four': event.members==4
    }
    
    
    return render(request,"events/event_registration.html", context)
