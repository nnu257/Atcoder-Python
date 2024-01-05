import numpy as np
import sys

A=[list(map(int,input().split())) for i in range(9)]
AT =  np.array(A).T.tolist()

for i in range(9):
    if len(set(A[i])) < 9 or len(set(AT[i])) < 9:
        print("No")
        sys.exit()
        
for i in range(3):
    for j in range(3):
        Tmp = [A[0+3*i][0+3*j], A[0+3*i][1+3*j], A[0+3*i][2+3*j], A[1+3*i][0+3*j], A[1+3*i][1+3*j], A[1+3*i][2+3*j], A[2+3*i][0+3*j], A[2+3*i][1+3*j], A[2+3*i][2+3*j]]
        if len(set(Tmp)) < 9:
            print("No")
            sys.exit()
            
print("Yes")