# 1011. A+B和C.py
# Created by liqiang on 05/01/2018.

n = int(input(''))
for i in range(n):
    a,b,c = map(int, (input('').split()))
    print('Case #{}: '.format(i+1), end='')
    if a+b>c:
        print('true')
    else:
        print('false')
