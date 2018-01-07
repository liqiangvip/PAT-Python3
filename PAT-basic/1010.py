# Untitled.py
# Created by liqiang on 05/01/2018.

data = list(map(int, input('').split()))
result = []
for i in range(0, len(data),2):
    a, n = data[i], data[i+1]
    if a == 0 and n ==0:
        result.extend([0,0])
        continue
    if a!=0 and n==0:
        continue
    result.extend([a*n, n-1])
print(' '.join(map(str, result)))