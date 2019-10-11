# LOGIC:Python program to print diffrence between sum of even array indices and
#sum of odd array indices

def solve(a):
    sumodd=0
    sumeven=0;
    for i in range(0,len(a)):
        if(i%2==0):
            sumeven+=a[i];
        else:
            sumodd+=a[i];

    return sumeven-sumodd

a = [200,100,1000,150,250]
print(solve(a))
