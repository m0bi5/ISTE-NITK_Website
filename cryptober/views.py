from django.shortcuts import render
from .models import *

# Create your views here.
def instructions(request):
    return render(request,'cryptober/instructions.html',{'team':team})

def questions(request,team,id):
    response = Response.objects.get(team__id=id)
    inputs = eval('response.input'+str(id)).strip().split()
    if request.method=='GET':
        return render(request,'cryptober/question'+str(id),{'inputs':inputs},'team':team)
    else:
        if len(inputs)!=5:
            query = request.POST.get('query',None)
            output = eval('func'+str(id)+'(query)')
            if output==-6942069:
                return render(request,'cryptober/error.html')
            #add to the stored inputs
            inputs = eval('response.input'+str(id)).strip().split()
        return render(request,'cryptober/question'+str(id),{'inputs':inputs})
