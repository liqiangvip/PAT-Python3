# Untitled.py
# Created by liqiang on 03/01/2018.

# Untitled.py
# Created by liqiang on 03/01/2018.

visited_values = set()    # 所有遍历过的数字的集合
key_values = []           # 关键数的列表

n = int(input(''))
nums = list(map(int, input('').split()))
for i in nums:
    if i not in visited_values: # 是集合中未出现的数字,添加到关键数,并进行3n+1的计算;否则不予理会
        key_values.append(i)
        r = i
        while r!=1:    # 进行计算,将途中出现的数字添加到集合中,直到结果为1
            visited_values.add(r)
            if r%2==0:
                r = r/2
            else:
                r = (3*r+1)/2
            if r in key_values:
                key_values.remove(r)

key_values.sort(reverse=True)
print(' '.join(map(str, key_values)))

    
