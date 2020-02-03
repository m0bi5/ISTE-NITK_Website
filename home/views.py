from django.shortcuts import render
from datetime import datetime
from account import models as account_models
from projects import models as project_models
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import os

def home(request):
    this_year=datetime.now().year
    years_in_operation=this_year-1995
    sigs=account_models.SIG.objects.all()
    member_count=len(account_models.User.objects.filter(batch_of__in=[this_year+3,this_year+2,this_year+1]))
    sig_count=len(account_models.SIG.objects.all())
    project_count=len(project_models.Project.objects.filter(year=this_year))
    core=account_models.Core.objects.all()
    context={'core':core,'sigs':sigs,'year':years_in_operation,'member':member_count,'sig':sig_count,'project':project_count}
    return render(request,'home/index.html',context)

@require_POST
@csrf_exempt
def webhook(request):
    os.system('sudo nohup ./deploy.sh &')
    print("Updated local repository...")
    return render(request,'home/index.html',{})