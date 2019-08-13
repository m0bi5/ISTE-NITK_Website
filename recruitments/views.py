from django.shortcuts import render_to_response,render,redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import ApplicantForm,recaptchaForm
from django.http import HttpResponseRedirect
from django.conf import settings
from .models import *
import urllib
import json
import smtplib
from email.mime.text import MIMEText as text
from django.contrib import messages
from django.template import RequestContext

# Create your views here.
def applicant_details(request,rollno):
    
    if request.method=='POST':
        form = ApplicantForm(request.POST)
        if form.is_valid():
            details = form.cleaned_data
            not_chosen = []
            chosen = []

            for i in details['sig_choices']:
                if len(ApplicantResponse.objects.filter(applicant__rollno=details['rollno'],sig_round=SIGRound.objects.filter(sig=i)[0]))==0:
                    not_chosen.append(str(i.id))
                else:
                    chosen.append(str(i.id))
            del details['sig_choices']

            if len(chosen)!=0 and len(not_chosen)>0:
                messages.add_message(request,messages.ERROR,"Cannot display questions for these SIGs as you've already submitted responses:{}".format(", ".join(chosen)))
            elif len(not_chosen)==0:
                messages.add_message(request,messages.INFO,"You have already applied for the selected SIGs")
                return render(request,'recruitments/finished.html')

            sigs = '&'.join(not_chosen)
            response=redirect('/recruitments/questions/{}/{}'.format(details['rollno'],sigs))
            response.set_cookie('details',str(details))
            return response
        else:
            print("sdgfbsjdknawmlkfbn")
            return render(request,'recruitments/applicant_deets.html',{'form':form})

    else:
        form = ApplicantForm()
        return render(request,'recruitments/applicant_deets.html',{'form':form})

def questions(request,applicant_rollno,sigs):
    if request.method=='GET':
        sig_choices=[account_models.SIG.objects.get(id=i) for i in sigs.split('&')]
        questions = {}
        for sig in sig_choices:
            questions[sig] = Question.objects.filter(sig_round=SIGRound.objects.get(sig=sig,round_number=1))
        return render(request,'recruitments/sig_questions.html',{'captcha':recaptchaForm,'questions':questions})
    else:
        details = eval(request.COOKIES['details'])
        applicant=None
        try:
            applicant = Applicant.objects.create(rollno=details['rollno'],first_name=details['first_name'],last_name=details['last_name'],phone=details['phone'],email=details['email'],year=details['year'])
        except:
            applicant = Applicant.objects.get(rollno=details['rollno'])
        sig_choices=[account_models.SIG.objects.get(id=i) for i in sigs.split('&')]
        for sig in sig_choices:
            ApplicantProgress.objects.create(applicant=applicant,sig=sig,round_completed=0,qualified_for_next=True)
        response = dict(request.POST.copy())
        quest_ids = list(response.keys())
        quest_ids.remove('csrfmiddlewaretoken')
        quest_ids.remove('g-recaptcha-response')
        quest_ids.remove('action')
        cc=0
        for id in quest_ids:
            question = Question.objects.get(id=int(id))
            if cc==0:
                ApplicantResponse.objects.create(applicant=applicant,response=response[id][0],question=question,sig_round=question.sig_round,disabled=False)
            else:
                ApplicantResponse.objects.create(applicant=applicant,response=response[id][0],question=question,sig_round=question.sig_round,disabled=True)
            cc+=1
        gmailaddress = "istenitkchapter@gmail.com"
        gmailpassword = "tqlsyhqfyskwutxh"
        mailto = applicant.email
        mailServer = smtplib.SMTP('smtp.gmail.com:587')
        mailServer.starttls()
        mailServer.login(gmailaddress , gmailpassword)

        msg = text('''Hey {}!\n\tThank you for participating in the recruitment process! Your progress will be uploaded soon, which can be viewed by clicking on this link: http://iste.nitk.ac.in/recruitments/progress/{}/'''.format(applicant.first_name,str(applicant.rollno)))
        msg['Subject'] = 'ISTE Recruitments - Applicant Progress'
        msg['From'] = gmailaddress
        msg['To'] = mailto
        mailServer.sendmail(gmailaddress, mailto , msg.as_string())
        mailServer.quit()
        return render(request,'recruitments/finished.html')
        
def application_progress(request,applicant_rollno):
    applicant=Applicant.objects.get(rollno=applicant_rollno)
    sigs_progress=ApplicantProgress.objects.filter(applicant=applicant)

    score_calculated=[]
    for progress in sigs_progress:
        other_applicants_progress=ApplicantProgress.objects.filter(sig=progress.sig,round_completed__gt=progress.round_completed).exclude(id=progress.id)
        if len(other_applicants_progress)>0:
            score_calculated.append(True)
        else:
            score_calculated.append(False)
    print('fknsdfsdbjkhgb sjhgbsdjkf',score_calculated)
    if len(score_calculated)==2:
        score_calculated=[True,True]
    return render(request,'recruitments/application_progress.html',{'applicant':applicant,'sigs_progress':zip(score_calculated,list(sigs_progress)),'applicant':applicant})

@login_required(login_url='/account/login')
def interview(request):
    applications=[]
    sigs=request.user.sigs.all()
    context={'interviewable':sigs}
    interviewable_sigs=[]
    return render(request,'recruitments/interview.html',context)

@login_required(login_url='/account/login')
def sig_interview(request,sig):
    applicants=ApplicantResponse.objects.filter(sig_round__sig__name=sig,sig_round__round_number=1).values_list('applicant', flat=True).distinct()
    applicants=[Applicant.objects.get(rollno=applicant) for applicant in applicants]
    progresses=[]
    for applicant in applicants:
        try:
            progress=ApplicantProgress.objects.get(applicant=applicant,sig__name=sig)
        except:
            print(applicant)
        if progress.interview_done:
            del applicants[applicants.index(applicant)]
        else:
            progresses.append(progress)

    context={'applicants':zip(applicants,progresses),'sig':sig}
    if request.POST:
        print(request.POST['rollno'])
        try:
            applicants=Applicant.objects.filter(rollno=request.POST['rollno'])
            if len(applicants)==0:
                messages.add_message(request,messages.ERROR,"Roll number not found")
            progress=ApplicantProgress.objects.filter(applicant=applicants[0],sig__name=sig)
            context['applicants']=zip(applicants,progress)
        except Exception as e:
            print(e)
            messages.add_message(request,messages.ERROR,"Roll number not found")
    return render(request,'recruitments/sig_interview.html',context)

@login_required(login_url='/account/login')
def edit_applicant(request,sig,rollno):
    applicant=Applicant.objects.get(rollno=rollno)
    applicant.rollno=request.POST['rollno']
    applicant.save()
    messages.add_message(request,messages.SUCCESS,"Applicant details edited")

    return redirect('personal_interview',sig,rollno)

@login_required(login_url='/account/login')
def personal_interview(request,sig,rollno):
    applicant=Applicant.objects.get(rollno=rollno)
    responses=ApplicantResponse.objects.filter(sig_round__sig__name=sig,sig_round__round_number=1,applicant=applicant)
    progress=ApplicantProgress.objects.get(sig__name=sig,applicant=applicant)
    sig_round=SIGRound.objects.get(sig__name=sig,round_number=progress.round_completed+1)
    criteria=Criteria.objects.filter(sig_round=sig_round)
    questions=Question.objects.filter(sig_round=sig_round)
    
    context={'questions':questions,'round_number':progress.round_completed+1,'sig':sig,'rollno':rollno,'applicant':applicant,'criteria':criteria,'sig_round':sig_round,'progress':progress,'responses':responses}
    if progress.interview_done:
        return redirect('sig_interview',sig)
    if request.POST:
        for crit in range(len(criteria)):
            if crit==0:
                InterviewResponse.objects.create(criteria=criteria[crit],response=request.POST[str(criteria[crit].id)],sig_round=sig_round,applicant=applicant,interviewer=request.user,disabled=False)
            else:
                InterviewResponse.objects.create(criteria=criteria[crit],response=request.POST[str(criteria[crit].id)],sig_round=sig_round,applicant=applicant,interviewer=request.user,disabled=True)
        progress.interview_done=True
        progress.save()
        return redirect('sig_interview',sig)

    return render(request,'recruitments/personal_interview.html',context)
