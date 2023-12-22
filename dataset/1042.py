import numpy as np

result = []

f2 = open('out.txt','w')

with open('1042.txt', 'r') as f:
    for line in f:
        result.append(line.strip().split(',')[0])
            #strip()去除空格和换行符
        print(result)
print(result, file=f2)

f2.close()