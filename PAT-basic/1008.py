# Untitled.py
# Created by liqiang on 03/01/2018.

# 题目要求只能用一个数组

x, y = list(map(int, input('').split()))
data = list(map(int, input('').split()))
for i in range(y):
    temp = data[-1]
    for j in range(x-1,0,-1):
        data[j] = data[j-1]
    data[0]=temp
print(' '.join(map(str, data)))