from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import ApplicantForm
from django.http import HttpResponseRedirect
from django.conf import settings
from .models import *
import urllib
import json
import smtplib
from email.mime.text import MIMEText as text
from django.contrib import messages

# Create your views here.
def applicant_details(request):
    if request.method=='POST':
        form = ApplicantForm(request.POST)
        if form.is_valid():
            details = form.cleaned_data
            applicant = Applicant.objects.filter(rollno=details['rollno'])
            if len(applicant)==0:
                applicant = Applicant.objects.create(rollno=details['rollno'],first_name=details['first_name'],last_name=details['last_name'],phone=details['phone'],email=details['email'],year=details['year'])
            else:
                applicant=applicant[0]
            not_chosen = []
            chosen = []

            for i in details['sig_choices']:
                if len(ApplicantResponse.objects.filter(applicant=applicant,sig=i))==0:
                    not_chosen.append(i)
                else:
                    chosen.append(i)
            if len(chosen)!=0 and len(not_chosen)>0:
                messages.add_message(request,messages.ERROR,"ERROR!!! Cannot display questions for these SIGs as you've already submitted responses:{}".format(", ".join(chosen)))
            elif len(not_chosen)==0:
                messages.add_message(request,messages.INFO,"YOU HAVE ALREADY SUBMITTED RESPONSES FOR ALL THE SELECTED SIGS!!!")
                return render(request,'recruitments/finished.html')
            sigs = '&'.join(not_chosen)

            return redirect('/recruitments/questions/{}/{}'.format(applicant.rollno,sigs))
    else:
        form = ApplicantForm()
    return render(request,'recruitments/applicant_deets.html',{'form':form})

def questions(request,applicant_rollno,sigs):
    if request.method=='GET':
        sig_choices = sigs.split('&')
        questions = {}
        for sig in sig_choices:
            questions[sig] = Question.objects.filter(sig=sig)
        return render(request,'recruitments/sig_questions.html',{'questions':questions})
    else:
        recaptcha_response = request.POST.get('g-recaptcha-response')
        url = 'https://www.google.com/recaptcha/api/siteverify'
        values = {
            'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
            'response': recaptcha_response
        }
        data = urllib.parse.urlencode(values).encode('utf-8')
        req = urllib.request.Request(url, data)
        response = urllib.request.urlopen(req)
        result = json.load(response)

        if result['success']:
            applicant = Applicant.objects.get(rollno=applicant_rollno)
            response = dict(request.POST.copy())
            quest_ids = list(response.keys())
            quest_ids.remove('csrfmiddlewaretoken')
            quest_ids.remove('g-recaptcha-response')
            for id in quest_ids:
                question = Question.objects.get(id=int(id))
                ApplicantResponse.objects.create(applicant=applicant,response=response[id][0],question=question,sig=question.sig)

            gmailaddress = "amodhshenoy@gmail.com"
            gmailpassword = "iwannaknow101"
            mailto = applicant.email

            mailServer = smtplib.SMTP('smtp.gmail.com' , 587)
            mailServer.starttls()
            mailServer.login(gmailaddress , gmailpassword)
            msg = text('''Hey {}!!\n\tThank you for participating in the recruitment process!!! Your applicant ID for the recruitment process is:{}'''.format(applicant.first_name,str(applicant.rollno)))
            msg['Subject'] = 'ISTE Recruitments - Applicant ID'
            msg['From'] = gmailaddress
            msg['To'] = mailto
            mailServer.sendmail(gmailaddress, mailto , msg.as_string())
            mailServer.quit()

            return render(request,'recruitments/finished.html')
        else:
            print("ERROR IN RECAPTCHA!")
            messages.add_message(request,messages.ERROR,"ERROR IN RECAPTCHA!! PLEASE TRY AGAIN!!")
            return redirect('/recruitments/questions/{}/{}'.format(applicant_rollno,sigs))

def application_progress(request,applicant_id):
    applicant=Applicant.objects.get(id=applicant_id)
    sigs_progress=ApplicantProgress.objects.filter(applicant=applicant)
    scores_calculated=[]
    #Get application of other people applied to the same sig and in the same round
    other_applicants_status=[ [applicant.qualified_for_next for applicant in ApplicantResponses.objects.filter(progress=obj.progress,sig=obj.sig).exclude(applicant=applicant)] for obj in sigs_progress]
    #If other people have qualified, applicant with applicant_id has not qualified
    for applicant_status in other_applicants_status:
        if True in applicant_status:
            scores_calculated.append(True)
        else:
            scores_calculated.append(False)

    return render(request,'recruitments/application_progress.html',{'progress_and_scores':zip(scores_calculated,sigs_progress)})

@login_required(login_url='/account/')
def interview(request):
    print(vars(request.user))
    return
