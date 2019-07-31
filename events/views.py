import json
import urllib

from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages
from .forms import RegistrationForm,TeamForm
from .models import Registration,Team,EventDetails
from .emailer import EmailHandler as em
from django.urls import reverse

# Create your views here.
def event_view(request):
    all_events=EventDetails.objects.all()
    context={
        'all_events':all_events
    }
    return render(request, "events/event_view.html",context)

def event_details(request, event_id):
    event=EventDetails.objects.get(id=event_id)
    return render(request, "events/event_details.html", {'event':event})

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
            team=Team.objects.create(event=event,team_name=request.POST['team_name'],member1=roll_no)
            team.save()
            messages.success(request,"Team successfully created!")
                
    return render(request, "events/event_teams.html",{'member1':roll_no,'form':TeamForm(),'event':event})

    

def event_register(request, event_id):
    event=EventDetails.objects.get(id=event_id)
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            obj=Registration(first_name=request.POST['first_name'],last_name=request.POST['last_name'],roll_no=request.POST['rollno'],email=request.POST['email'],phone=request.POST['phone'],event=event)
            obj.save()
            em_obj=em()
            link=request.build_absolute_uri(reverse('event_form_team',args=(event_id,request.POST['rollno'],)))
            em_obj.send_email(request.POST['email'],"You have registered for ISTE NITK's "+event.event_name,"Hello "+request.POST['first_name']+"!\n Thank you for registering for "+event.event_name+" which will be held on "+str(event.event_date)+"\n Form your teams here : "+link,'istenitkchapter@gmail.com','tqlsyhqfyskwutxh')
            messages.success(request, 'Success! You may now create a team by clicking the link in the email')
        else:
            messages.error(request, 'Invalid reCAPTCHA. Please try again.')

            return redirect(event_register,event_id)
    else:
        form = RegistrationForm()

    context = {
        'form': form
    }
    
    
    return render(request,"events/event_registration.html", context)