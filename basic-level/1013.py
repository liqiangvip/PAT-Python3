# 1013. 数素数.py
# Created by liqiang on 22/01/2018.

from math import sqrt
result =[2]
M, N = map(int, input().split())
count = 1
for x in range(3, 10000,2):
    for i in range(2, int(sqrt(x))+1):
        if x%i==0:
            break
    else:
        result.append(x)
        count += 1
        if count > N:
            break

for p, v in enumerate(result[M-1:N]):
    print(v, end='')
    if (p+1)%10 ==0:
        print()
    elif p<N-M:
        print(' ', end='')
    else:
        break
