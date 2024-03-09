n=int(input())
A=list(map(int,input().split()))
m=int(input())
B=list(map(int,input().split()))
l=int(input())
C=list(map(int,input().split()))
q=int(input())
X=list(map(int,input().split()))

can = set()
for i in range(n):
    for j in range(m):
        for k in range(l):
            can.add(A[i]+B[j]+C[k])
            
for i in range(q):
    if X[i] in can:
        print("Yes")
    else:
        print("No")