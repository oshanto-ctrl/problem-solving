# problem link:

def getncr(n, r):
    if r == 0 or r == n:
        return 1
    if r == 1 or r == n - 1:
        return n
    if r > n or n < 0 or r < 0:
        return 0
    
    return getncr(n-1, r-1) + getncr(n-1, r)

n = 5
r = 2
answer = getncr(n, r)
print(f"nCr-> {n}c{r} = {answer}")