from django.shortcuts import render
from django.views.generic import CreateView
from .models import Project
import datetime
# Create your views here.
def projects(request):
    projects_list = {}
    year_list = [r for r in range(2018, datetime.date.today().year +1)]
    for year in year_list:
        projects_list[year] = {}
        sigs = ['Crypt','Charge','Credit','Chronicle','Clutch','Concrete','Create','Catalyst']
        for sig in sigs:
            projects_list[year][sig] = Project.objects.filter(year=year,sig=sig)
<<<<<<< HEAD
=======
    print(projects_list)
>>>>>>> efcb0f26f8d46ae67ab1d5d3af81da4956b94641
    return render(request,'projects/project_list.html',{'projects': projects_list})

def show_project(request,id):
    project=Project.objects.get(id=id)
    return render(request,'projects/project.html',{'project':project})
