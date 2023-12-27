import math

n=int(input())

tmp=math.floor(math.sqrt(n))
while tmp > 0:
    if n%tmp == 0:
        print(len(str(n//tmp)))
        break
    
    tmp -= 1