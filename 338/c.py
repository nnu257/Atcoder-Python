import math

n=int(input())
Q=list(map(int,input().split()))
A=list(map(int,input().split()))
B=list(map(int,input().split()))

q_a = [math.floor(Q[i]/A[i]) if A[i] != 0 else 100000000 for i in range(n)]
tmp_x = min(q_a)
ans = 0

while tmp_x >= 0:
    
    left = [Q[i]-tmp_x*+A[i] for i in range(n)]
    canmake = [math.floor(left[i]/B[i]) if B[i] != 0 else 100000000 for i in range(n)]
    y = min(canmake)
    
    ans = max(ans, tmp_x+y)
    
    tmp_x -= 1
    
print(ans)