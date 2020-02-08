from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from datetime import datetime
# Create your views here.
def login(request):
    if request.method=='GET':
        # team=request.session['team']
        teams = Team.objects.all().order_by('-points','finish_time','-lives')
        return render(request,'obscura/leaderboard.html',{'lboard':teams[:3]})
        #return render(request,'obscura/.html')
    else:
        team = request.POST.get('team').strip()
        pwd = request.POST.get('pwd').strip()
        obj = Team.objects.filter(name=team,pwd=pwd)
        if len(obj)==1:
            obj = obj[0]
            request.session['team']=team
            return render(request,'obscura/home.html',{'team':team,'points':obj.points,'hearts':obj.lives})
        else:
            messages.error(request,'Invalid login credentials!')
            return render(request,'obscura/login.html')

def home(request,team):
    team=request.session['team']
    obj = Team.objects.filter(name=team)
    if len(obj)==1:
        obj = obj[0]
        return render(request,'obscura/home.html',{'team':team,'points':obj.points,'hearts':obj.lives})
    else:
        messages.error(request,'Invalid login credentials!')
        return render(request,'obscura/login.html')

def instructions(request,team):
    team=request.session['team']
    return render(request,'obscura/instructions.html',{'team':team})

def mini_games(request,team):
    team=request.session['team']
    return render(request,'obscura/mg_menu.html',{'team':team})

def quests_menu(request,team):
    team=request.session['team']
    obj = Team.objects.filter(name=team)
    if len(obj)==1:
        obj=obj[0]
        return render(request,'obscura/quests_menu.html',{'team':team,'med':obj.med_un,'hard':obj.hard_un,'points':obj.points,'hearts':obj.lives})
    else:
        messages.error(request,'Invalid login credentials!')
        return render(request,'obscura/login.html')

def snake(request,team):
    team=request.session['team']
    obj = Team.objects.filter(name=team)
    if len(obj)==1:
        obj = obj[0]
        if obj.points>=10:
            obj.points-=10
            obj.lives+=1
            obj.save()
            return render(request,'obscura/snek.html',{'team':team})
        else:
            messages.error(request,'Not enough points! Finish quests to earn points!')
            return render(request,'obscura/quests_menu.html',{'team':team,'med':obj.med_un,'hard':obj.hard_un,'points':obj.points,'hearts':obj.lives})
    else:
        messages.error(request,'Invalid login credentials!')
        return render(request,'obscura/login.html')

def maze(request,team):
    team=request.session['team']
    obj = Team.objects.filter(name=team)
    if len(obj)==1:
        obj = obj[0]
        if obj.points>=10:
            obj.points-=10
            obj.lives+=1
            obj.save()
            return render(request,'obscura/maze.html',{'team':team})
        else:
            messages.error(request,'Not enough points! Finish quests to earn points!')
            return render(request,'obscura/quests_menu.html',{'team':team,'med':obj.med_un,'hard':obj.hard_un,'points':obj.points,'hearts':obj.lives})
    else:
        messages.error(request,'Invalid login credentials!')
        return render(request,'obscura/login.html')

def fbird(request,team):
    team=request.session['team']
    obj = Team.objects.filter(name=team)
    if len(obj)==1:
        obj = obj[0]
        if obj.points>=10:
            obj.points-=10
            obj.lives+=1
            obj.save()
            return render(request,'obscura/fbird.html',{'team':team})
        else:
            messages.error(request,'Not enough points! Finish quests to earn points!')
            return render(request,'obscura/quests_menu.html',{'team':team,'med':obj.med_un,'hard':obj.hard_un,'points':obj.points,'hearts':obj.lives})
    else:
        messages.error(request,'Invalid login credentials!')
        return render(request,'obscura/login.html')


def done(team):
    obj = Team.objects.filter(name=team)
    if len(obj)==1:
        obj=obj[0]
        easy = eval(obj.easy_subs)
        med = eval(obj.med_subs)
        hard = eval(obj.hard_subs)
        if '*' not in easy and '*' not in med and '*' not in hard:
            obj.finish_time = str(datetime.now())
            return True
    else:
        messages.error(request,'Invalid login credentials!')
        return render(request,'obscura/login.html')

    return False


def easy(request,team,id):
    team=request.session['team']
    obj = Team.objects.filter(name=team)
    if len(obj)==1:
        obj=obj[0]
        subs = eval(obj.easy_subs)
        if request.method=='GET':
            if obj.lives>0:
                subbd = False if subs[int(id)-1]=='*' else True
                return render(request,'obscura/easy/'+id+'.html',{'team':team,'subbd':subbd,'hearts':obj.lives,'points':obj.points})
            else:
                messages.error(request,'You have run out of hearts! Play some mini games to earn hearts!')
                return render(request,'obscura/mg_menu.html',{'team':team})
        else:
            ans = request.POST.get('ans').strip()
            l = ['1','5','1','3','4','16=8+8','match']
            if ans==l[int(id)-1]:
                subbd = True
                subs[int(id)-1]=ans
                obj.easy_subs = str(subs)
                obj.points += 25
                obj.save()
                if done(team):
                    messages.success(request,"You have answered all the questions!! Check out your ranking in the leaderboard!!")
                    teams = Team.objects.all().order_by('-points','finish_time','-lives')
                    return render(request,'obscura/leaderboard.html',{'team':team,'lboard':teams})
                if '*' not in subs:
                    messages.success(request,'You have answered all Easy quests! Medium Level unlocked!')
                    obj.med_un=True
                    obj.save()
                    return render(request,'obscura/quests_menu.html',{'team':team,'med':obj.med_un,'hard':obj.hard_un,'points':obj.points,'hearts':obj.lives})

            else:
                messages.error(request, 'Wrong Answer! Try again!')
                subbd = False
                obj.lives -=1
                obj.save()
            if obj.lives>0:
                return render(request,'obscura/easy/'+id+'.html',{'team':team,'subbd':subbd,'hearts':obj.lives,'points':obj.points})
            else:
                messages.error(request,'You have run out of hearts! Play some mini games to earn hearts!')
                return render(request,'obscura/mg_menu.html',{'team':team})
    else:
        messages.error(request,'Invalid login credentials!')
        return render(request,'obscura/login.html')


def med(request,team,id):
    team = request.session['team']
    obj = Team.objects.filter(name=team)
    if len(obj)==1:
        obj=obj[0]
        subs = eval(obj.med_subs)
        if obj.med_un:
            if request.method=='GET':
                if obj.lives>0:
                    subbd = False if subs[int(id)-1]=='*' else True
                    return render(request,'obscura/med/'+id+'.html',{'team':team,'subbd':subbd,'hearts':obj.lives,'points':obj.points})
                else:
                    messages.error(request,'You have run out of hearts! Play some mini games to earn hearts!')
                    return render(request,'obscura/mg_menu.html',{'team':team})
            else:
                ans = request.POST.get('ans').strip()
                l = ['17','1009','33','833','5','4213567','1']
                if ans==l[int(id)-1]:
                    subbd = True
                    subs[int(id)-1]=ans
                    obj.med_subs = str(subs)
                    obj.points+=40
                    obj.save()

                    if done(team):
                        messages.success(request,"You have answered all the questions!! Check out your ranking in the leaderboard!!")
                        teams = Team.objects.all().order_by('-points','finish_time','-lives')
                        return render(request,'obscura/leaderboard.html',{'team':team,'lboard':teams})
                    if '*' not in subs:
                        messages.success(request,'You have answered all Medium quests! Hard Level unlocked!')
                        obj.hard_un=True
                        obj.save()
                        return render(request,'obscura/quests_menu.html',{'team':team,'med':obj.med_un,'hard':obj.hard_un,'points':obj.points,'hearts':obj.lives})
                else:
                    messages.error(request, 'Wrong Answer! Try again!')
                    subbd = False
                    obj.lives-=1
                    obj.save()
                if obj.lives>0:
                    return render(request,'obscura/med/'+id+'.html',{'team':team,'subbd':subbd,'hearts':obj.lives,'points':obj.points})
                else:
                    messages.error(request,'You have run out of hearts! Play some mini games to earn hearts!')
                    return render(request,'obscura/mg_menu.html',{'team':team})
        else:
            messages.error(request,'Medium quests locked!')
            return render(request,'obscura/quests_menu.html',{'team':team,'med':obj.med_un,'hard':obj.hard_un,'points':obj.points,'hearts':obj.lives})
    else:
        messages.error(request,'Invalid login credentials!')
        return render(request,'obscura/login.html')


def hard(request,team,id):
    team=request.session['team']
    obj = Team.objects.filter(name=team)
    if len(obj)==1:
        obj=obj[0]
        subs = eval(obj.hard_subs)
        if obj.hard_un:
            if request.method=='GET':
                if obj.lives>0:
                    subbd = False if subs[int(id)-1]=='*' else True
                    return render(request,'obscura/hard/'+id+'.html',{'team':team,'subbd':subbd,'hearts':obj.lives,'points':obj.points})
                else:
                    messages.error(request,'You have run out of hearts! Play some mini games to earn hearts!')
                    return render(request,'obscura/mg_menu.html',{'team':team})
            else:
                ans = request.POST.get('ans').strip()
                l = ['blue','33%','6210001000','140','9','tuesday','hospital']
                if ans==l[int(id)-1]:
                    subbd = True
                    subs[int(id)-1]=ans
                    obj.hard_subs = str(subs)
                    obj.points+=60
                    obj.save()
                    if done(team):
                        messages.success(request,"You have answered all the questions!! Check out your ranking in the leaderboard!!")
                        teams = Team.objects.all().order_by('-points','finish_time','-lives')
                        return render(request,'obscura/leaderboard.html',{'team':team,'lboard':teams})
                else:
                    messages.error(request, 'Wrong Answer! Try again!')
                    subbd = False
                    obj.lives-=1
                    obj.save()
                if obj.lives>0:
                    return render(request,'obscura/hard/'+id+'.html',{'team':team,'subbd':subbd,'hearts':obj.lives,'points':obj.points})
                else:
                    messages.error(request,'You have run out of hearts! Play some mini games to earn hearts!')
                    return render(request,'obscura/mg_menu.html',{'team':team})
        else:
            messages.error(request,'Hard quests locked!')
            return render(request,'obscura/quests_menu.html',{'team':team,'med':obj.med_un,'hard':obj.hard_un,'points':obj.points,'hearts':obj.lives})
    else:
        messages.error(request,'Invalid login credentials!')
        return render(request,'obscura/login.html')


def un_med(request,team):
    obj = Team.objects.filter(name=team)[0]
    if obj.lives>=10:
        obj.lives-=10
        obj.med_un = True
        obj.save()
        return render(request,'obscura/quests_menu.html',{'team':team,'med':obj.med_un,'hard':obj.hard_un,'points':obj.points,'hearts':obj.lives})
    else:
        messages.error(request,'Not enough hearts! Play mini games to earn hearts!')
        return render(request,'obscura/quests_menu.html',{'team':team,'med':obj.med_un,'hard':obj.hard_un,'points':obj.points,'hearts':obj.lives})


def lboard(request,team):
    team=request.session['team']
    teams = Team.objects.all().order_by('-points','finish_time','-lives')
    return render(request,'obscura/leaderboard.html',{'team':team,'lboard':teams})

def un_hard(request,team):
    obj = Team.objects.filter(name=team)[0]
    if obj.lives>=15:
        obj.lives-=15
        obj.hard_un = True
        obj.save()
        return render(request,'obscura/quests_menu.html',{'team':team,'med':obj.med_un,'hard':obj.hard_un,'points':obj.points,'hearts':obj.lives})
    else:
        messages.error(request,'Not enough hearts! Play mini games to earn hearts!')
        return render(request,'obscura/quests_menu.html',{'team':team,'med':obj.med_un,'hard':obj.hard_un,'points':obj.points,'hearts':obj.lives})
