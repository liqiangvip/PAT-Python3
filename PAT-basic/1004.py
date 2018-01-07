# Untitled.py
# Created by liqiang on 03/01/2018.

n = int(input(''))
data = []
for i in range(n):
    name, id, score = input('').split()
    score = int(score)
    data.append((name, id, score))

data.sort(key=lambda item:item[2])
print(data[-1][0], data[-1][1])
print(data[0][0], data[0][1])