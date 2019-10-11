from django.shortcuts import render,redirect
from .models import *

def instructions(request):
    if request.method=='GET':
        return render(request,'cryptober/instructions.html')
    else:
        name = request.POST.get('name').strip()
        email = request.POST.get('email')
        Response.objects.create(name=name,email=email)
        return redirect(name+'/questions/1')

def questions(request,team,id):
    try:
        response = Response.objects.get(name=team)
        # print("GOT IT",len(response.input1))
        prev_inputs = eval('response.input'+id)
        prev_inputs = eval(prev_inputs)
        # print(type(prev_inputs))
        if request.method=='GET':
            return render(request,'cryptober/question'+id+'.html',{'inputs':prev_inputs,'team':team})
        else:
            if len(prev_inputs)<5:
                query = request.POST.get('query',None).strip().split()
                # print(type())
                query,output = eval('func'+id+'(query)')
                if output==-6942069:
                    return render(request,'cryptober/error.html')
                query.append(output)
                prev_inputs.append(query)
                if id=='1':
                    response.input1 = prev_inputs
                elif id=='2':
                    response.input2 = prev_inputs
                elif id=='3':
                    response.input3 = prev_inputs
                elif id=='4':
                    response.input4 = prev_inputs
                elif id=='5':
                    response.input5 = prev_inputs
                response.save()
            return render(request,'cryptober/question'+str(id)+'.html',{'inputs':prev_inputs,'team':team})
    except:
        return render(request,'cryptober/error.html')

#Logic: This program prints the difference of cube
#of number having maximum absolute value and minimum absolute value.
def func1(a):
    if len(a)!=5:
        return -6942069
    minv=int(a[0])
    maxv=int(a[0])
    for i in a:
        if i.isdigit():
            i=int(i)
            minv=min(minv,abs(i))
            maxv=max(maxv,abs(i))
        else:
            return -6942069
    return a,(maxv*maxv*maxv-minv*minv*minv)

#Logic: Print no. of characters that have count more than 1
def func2(query):
    if len(query)!=1:
        return -6942069
    query = query[:1]
    count = [0] * 256
    for i in query[0]:
        count[ord(i)] += 1
    k = 0
    cnt=0
    for i in count:
        if int(i) > 1:
            cnt=cnt+1
    return query,cnt

# Logic:A Dynamic Programming based Python program for edit
# distance problem :
# minimum number of edits (operations) required to convert ‘str1’ into ‘str2’.
#allowed operations:
#Insert
#Remove
#Replace
def func3(query):
    if len(query)<2:
        return -6942069
    query = query[:2]
    str1 = query[0]
    str2 = query[1]
    m = len(str1)
    n = len(str2)
    dp = [[0 for x in range(n+1)] for x in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i][j-1],
								dp[i-1][j],
								dp[i-1][j-1])
    return query,dp[m][n]

# Logic:Dynamic programming Python implementation of LIS problem
# lis returns length of the longest increasing subsequence
# in arr of size n
def func4(arr):
    if len(arr)!=7:
        return -6942069
    n = len(arr)
    for i in range(n):
        arr[i] = int(arr[i])
    lis = [1]*n
    for i in range (1 , n):
        for j in range(0 , i):
            if arr[i] > arr[j] and lis[i]< lis[j] + 1 :
                lis[i] = lis[j]+1
    maximum = 0
    for i in range(n):
	       maximum = max(maximum , lis[i])
    return arr,maximum

# LOGIC:Python program to print diffrence between sum of even array indices and
#sum of odd array indices
def func5(a):
    if len(a)!=5:
        return -6942069
    for i in range(len(a)):
        a[i] = int(a[i])
    sumodd=0
    sumeven=0
    for i in range(0,len(a)):
        if(i%2==0):
            sumeven+=a[i]
        else:
            sumodd+=a[i]
    return a,sumeven-sumodd
