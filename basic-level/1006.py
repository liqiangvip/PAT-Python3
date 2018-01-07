# 1006. 换个格式输出整数.py
# Created by liqiang on 05/01/2018.

data = list(input(''))
result = ''.join(map(str, range(1,int(data[-1])+1)))
for ch, num in zip('SB', data[:-1][::-1]):
    result = int(num)*ch + result
print(result)