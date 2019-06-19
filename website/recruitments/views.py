from django.shortcuts import render
#from .models import ApplicantPasscode
import hashlib
from .models import *

# Create your views here.
def recruitments(request):
    return

def application_progress(request,applicant_id):
    applicant=Applicant.objects.get(id=applicant_id)
    sigs_progress=ApplicantResponses.objects.filter(applicant=applicant)
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