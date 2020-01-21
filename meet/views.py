from django.shortcuts import render
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import datetime,date


@login_required(login_url='/account/login')
def view_meets(request):
    if request.method=='GET':
        objs = Meet.objects.all()
        l = []
        today = date.today()
        for meet in objs:
            if meet.date>=today:
                l.append(meet)
        objs = l
        empty = True if len(objs)==0 else False
        meets = {}
        for meet in objs:
            if meet.date in meets.keys():
                meets[meet.date].append(meet)
            else:
                meets[meet.date]=[meet]
        dict = {'meets':meets,
                'senior':request.user.batch_of<2022,
                'empty':empty}
        return render(request,'meet/view.html',dict)

@login_required(login_url='/account/login')
def add_meet(request):
    if request.method=='GET':
        if request.user.batch_of<2022:
            form = MeetForm()
            return render(request,'meet/create_meet.html',{'form':form})
        else:
            messages.error(request,'Only 3rd and 4th year members can access this page!')
            return redirect('/meets/')
    elif request.method=='POST':
        form = MeetForm(request.POST)
        if form.is_valid():
            date = datetime.strptime(request.POST['date_year']+'-'+request.POST['date_month']+'-'+request.POST['date_day'],'%Y-%M-%d').date()
            start_time = datetime.strptime(request.POST['start_time'][:5],'%H:%M').time()
            end_time = datetime.strptime(request.POST['end_time'][:5],'%H:%M').time()
            objs = Meet.objects.all()
            safe = True
            #check if date is valid
            if start_time>=end_time:
                safe=False
                messages.error(request,'Start time has to be before End time! Please check again!')
                print(form.errors)
                return render(request,'meet/create_meet.html',{'form':form})
            if len(objs)>0:
                for meet in objs:
                    if meet.date==date:
                        if meet.start_time==start_time and meet.end_time==end_time:
                            safe=False
                            break
                        elif meet.end_time>start_time and meet.start_time<start_time:
                            safe=False
                            break
                        elif meet.start_time<end_time and meet.end_time>end_time:
                            safe=False
                            break
            if safe:
                meet = Meet(member=User.objects.get(id=request.user.id),venue=request.POST['venue'],topic=request.POST['topic'],date=request.POST['date_year']+'-'+request.POST['date_month']+'-'+request.POST['date_day'],start_time=request.POST['start_time'],
                        end_time=request.POST['end_time'],sig=request.POST['sig'])
                meet.save()
                messages.success(request,'Meet added successfully!')
                return render(request,'meet/create_meet.html',{'form':form})
        messages.error(request,'Invalid input(s)! Please check again!')
        print(form.errors)
        return render(request,'meet/create_meet.html',{'form':form})
