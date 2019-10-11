#Logic: Print no. of charaters that are repeated  passed string

def printDups(string):
    count = [0] * 256
    for i in string:
        count[ord(i)] += 1
    k = 0
    cnt=0;
    for i in count:
        if int(i) > 1:
            cnt=cnt+1;
    return cnt;



# Driver program to test the above function
string = ['a','a']
print(printDups(string))
