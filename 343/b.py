n = int(input())
A = [list(map(int,input().split())) for i in range(n)]

for i in range(n):
    ad = [str(j+1) for j in range(n) if A[i][j]==1]
    print(" ".join(ad))