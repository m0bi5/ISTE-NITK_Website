from django.shortcuts import render
from django.views.generic import CreateView
from .models import Project
from account import models as account_models
import datetime
# Create your views here.
def projects(request):
    projects_list = {}
    year_list = [r for r in range(2018, datetime.date.today().year)]
    for year in year_list:
        projects_list[year] = {}
        sigs = ['Crypt','Charge','Credit','Chronicle','Clutch','Concrete','Create','Catalyst']
        for sig in account_models.SIG.objects.all():
            projects_list[year][sig] = Project.objects.filter(year=year,sig=sig)
    return render(request,'projects/project_list.html',{'projects': projects_list})

def show_project(request,id):
    project=Project.objects.get(id=id)
    project.tags=project.tags.split(';')
    return render(request,'projects/project.html',{'project':project})
