# 1012. 数字分类.py
# Created by liqiang on 05/01/2018.

def avg(x):
    return sum(x)/len(x)

x = list(map(int, input('').split()))[1:]
a1 = [i for i in x if i%5==0 and i%2==0]
a2 = [i for i in x if i%5==1]
a3 = [i for i in x if i%5==2]
a4 = [i for i in x if i%5==3]
a5 = [i for i in x if i%5==4]

if a1==[]:
    r1 = 'N'
else:
    r1 = sum(a1)

if a2==[]:
    r2 = 'N'
else:    
    r2 = 0
    for p,v in enumerate(a2):
        r2 += v*(-1)**p

if a3==[]:
    r3 = 'N'
else:
    r3 = len(a3)

if a4==[]:
    r4 = 'N'
else:
    r4 = '%.1f'%(avg(a4))

if a5 ==[]:
    r5 = 'N'
else:
    r5 = max(a5)

print(r1, r2, r3, r4, r5)
