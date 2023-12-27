import numpy as np
import sys

C1=np.array(list(map(int,input().split())))
C2=np.array(list(map(int,input().split())))
C3=np.array(list(map(int,input().split())))

C_1=np.array([C1[0], C2[0], C3[0]])
C_2=np.array([C1[1], C2[1], C3[1]])
C_3=np.array([C1[2], C2[2], C3[2]])

if len(set(C1-C2)) == 1:
    if len(set(C2-C3)) == 1:
        if len(set(C3-C1)) == 1:
            if len(set(C_1-C_2)) == 1:
                if len(set(C_2-C_3)) == 1:
                    if len(set(C_3-C_1)) == 1:
                        print("Yes")
                        sys.exit()
print("No")
