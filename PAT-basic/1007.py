# Untitled.py
# Created by liqiang on 03/01/2018.

from math import sqrt

def isPrime(x):
    if x < 2:
        return Fales
    for i in range(2, int(sqrt(x)+1)):
        if x%i ==0:
            return False
    return True
    
n = int(input(''))
count = 0
for i in range(3,n,2):
    if isPrime(i) and isPrime(i+2):
        count +=1
print(count)
