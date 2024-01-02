n,l,r=map(int,input().split())
A=list(map(int,input().split()))

answer = [0 for i in range(n)]
for i in range(n):
    if A[i] < l:
        answer[i] = l
    elif r < A[i]:
        answer[i] = r
    else:
        answer[i] = A[i]
        
print(*answer)