n=int(input())
A=list(map(int, input().split()))

A=sorted(list(set(A)), reverse=True)
print(A[1])