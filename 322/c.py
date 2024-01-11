n,m=map(int,input().split())
A=list(map(int,input().split()))
A=[a-1 for a in A]

tmp = 0
A_tmp = A[tmp]
for i in range(n):
    if i == A_tmp:
        print(0)
        tmp += 1
        if tmp <= m-1:
            A_tmp = A[tmp]
    else:
        print(A_tmp-i)