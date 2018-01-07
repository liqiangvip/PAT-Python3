# Untitled.py
# Created by liqiang on 03/01/2018.

count = 0

#def callatz(n):
#    global count
#    count += 1
#    if n%2==0:
#        return n/2
#    else:
#        return (3*n+1)/2

def callatz2(n):
    global count
    print(n)
    if n ==1:
        return
    else:
        count += 1
    if n%2==0:
        callatz2(n/2)
    else:
        callatz2((3*n+1)/2)

n = int(input(''))
callatz2(n)
