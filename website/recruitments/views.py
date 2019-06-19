from django.shortcuts import render
#from .models import ApplicantPasscode
import hashlib

# Create your views here.
def recruitments(request):
    return

def application_progress(request,applicant_id):
    #applicant=ApplicantPasscode.objects.get(applicant_id=applicant_id)
    #return render(request,'recruitments/application_progress.html',{'applicant_passcode':hashlib.sha256(applicant_passcode.encode()).hexdigest()})
    return