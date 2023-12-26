import sys

n,y=map(int,input().split())

'''
for i in range(n):
    for j in range(n):
        for k in range(n):
            if i+j+k==n and 10000*i+5000*j+1000*k==y:
                print(f"{i} {j} {k}")
                sys.exit()
'''
'''
A = np.array([[[0 for i in range(n+1)] for i in range(n+1)] for i in range(n+1)])

for i in range(n):
    for j in range(n):
        A[i][j][0] = 10000*i+5000*j
        for k in range(1,n):
            if A[i][j][k-1] > y or i+j+k>n:
                break
            A[i][j][k] = A[i][j][k-1] + 1000

ind = np.argwhere(A==y)[0]
print(ind)
''' 
for i in range(n+1):
    for j in range(n+1):
        k = n-i-j
        if k>=0 and 10000*i+5000*j+1000*k==y:
            print(f"{i} {j} {k}")
            sys.exit()

print("-1 -1 -1")

