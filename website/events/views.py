import json
import urllib

from django.shortcuts import render, redirect
from django.cong import settings
from django.contrib import messages
from .forms import Registrationform
from .models import Registration, EventDetails
from .emailer import EmailHandler as em


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


def event_register(request, event_id):
    obj = Registration.objects.get(id=event_id)
    if request.method == 'POST':
        form = Registrationform(request.POST or None, instance=obj)
        if form.is_valid():
            recaptcha_response = request.POST.get('g-recaptcha-response')
            url = 'https://www.google.com/recaptcha/api/siteverify'
            values = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
            data = urllib.parse.urlencode(values).encode()
            req =  urllib.request.Request(url, data=data)
            response = urllib.request.urlopen(req)
            result = json.loads(response.read().decode())
            if result['success']:
                form.save()
                em_obj=em()
                em_obj.send_mail('obj.email'," "," ",'mobits.bot@gmail.com','mobits123')
                messages.success(request, 'Success!')
            else:
                messages.success(request, 'Invalid reCAPTCHA. Please try again.')
    
            return redirect(event_register,event_id)
    else:
    form = Registrationform()

    context = {
        'form': form

    }
    
    
    return render(request,"events/event_registration.html", context)