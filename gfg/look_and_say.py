"""
def lookNsay(n):
    result = ""
    repeat = n[0]
    n = n[1:]+" "
    times = 1

    for actual in n:
        if actual != repeat:
            result += str(times)+repeat
            times = 1
            repeat = actual
        else:
            times += 1
    return result

num = "5"
print(f"Result = {lookNsay(num)}")
"""
from itertools import groupby
def lookNsay(n):
    k, last, result, a = 1, '', '', str(n)
    for i in range(len(n)):
        if last == n[i]:
            k+=1
        else:
            result = result + str(k)+n[i]
            k=1
        last = n[i]
    return int(result)

n = "2"
res = lookNsay(n)
print(f"Result = {res} type of result = {type(res)}")
