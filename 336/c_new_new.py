import numpy as np
n=int(input())

nn = np.base_repr(n-1, 5)

nn = list(str(nn))
for i in range(len(nn)):
    nn[i] = str(int(nn[i])*2)
    
print("".join(nn))