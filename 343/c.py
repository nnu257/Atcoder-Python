import math

n = int(input())
ri_n = math.ceil(math.pow(n, 1/3))

def check_kai(n):
    n = str(n)
    if n == n[::-1]:
        return True

for i in range(ri_n, -1, -1):
    
    k = i**3
    #print(i, k)
    if k <= n:
        if check_kai(k):
            print(k)
            exit()