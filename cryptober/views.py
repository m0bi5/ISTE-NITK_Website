from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def instructions(request):
    if request.method=='GET':
        return render(request,'cryptober/instructions.html')
    else:
        name = request.POST.get('name').strip()
        email = request.POST.get('email')
        Response.objects.create(name=name,email=email)
        return redirect(name+'/questions/1')

def func1(query):
    pass

def func2(query):
    pass

def func3(query):
    pass

def func4(query):
    pass

def func5(query):
    pass

def questions(request,team,id):
    response = Response.objects.get(name=team)
    prev_inputs = eval(eval('response.input'+str(id)))
    if request.method=='GET':
        return render(request,'cryptober/question'+str(id)+'.html',{'inputs':prev_inputs,'team':team})
    else:
        if len(prev_inputs)<5:
            query = request.POST.get('query',None).strip().split()
            output = eval('func'+str(id)+'(query)')
            if output==-6942069:
                return render(request,'cryptober/error.html')
            query.append(output)
            eval('response.input'+str(id)+'=prev_inputs.append(query)')
        return render(request,'cryptober/question'+str(id)+'.html',{'inputs':prev_inputs,'team':team})
