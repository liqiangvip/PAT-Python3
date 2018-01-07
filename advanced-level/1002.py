# 1002. A+B for Polynomials.py
# Created by liqiang on 06/01/2018.

from decimal import *

a = list(map(Decimal, input().split()))
b = list(map(Decimal, input().split()))

d1 = {a[i]:a[i+1] for i in range(len(a)) if i%2==1 }
d2 = {b[i]:b[i+1] for i in range(len(b)) if i%2==1 }
d = {}
for k in list(d1.keys())+list(d2.keys()):
    d[int(k)] = d1.get(k, 0) + d2.get(k,0)

if 0 in d and d[0]==0:
    del d[0]
result = []
result.append(len(d))
for n, a in sorted(d.items(), reverse=True):
    result += [n, a]
print(' '.join(map(str, result)))
