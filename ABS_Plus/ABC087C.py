n=int(input())
A1=list(map(int,input().split()))
A2=list(map(int,input().split()))
A=[A1,A2]
'''
candy = 0
tmp = 0
for move_down in range(n):
    tmp = 0
    for i in range(n):
        h = 1 if i>=move_down else 0
        tmp += A[h][i]
        if i==move_down:
            tmp += A[0][i]
    if tmp > candy:
        candy = tmp
        
print(candy)
'''

DP=[[0 for i in range(n)], [0 for i in range(n)]]
DP[0][0] = A[0][0]
for i in range(1,n):
    DP[0][i] = DP[0][i-1]+A[0][i]
DP[1][0] = DP[0][0]+A[1][0]
for i in range(1,n):
    DP[1][i] = max(DP[0][i], DP[1][i-1])+A[1][i]
    
print(DP[1][n-1])