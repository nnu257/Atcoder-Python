import sys
h,w=map(int,input().split())
S = [list(input()) for i in range(h)]

def white(i,j):
    if 0<=i<=h-1 and 0<=j<=w-1:
        if S[i][j] == "#":
            return False
        
    return True

#print(S)

for i in range(h):
    for j in range(w):
        #print(f"{i} {j}")
        if S[i][j] == "#":
            if white(i-1, j) and white(i,j-1) and white(i+1,j) and white(i,j+1):
                print("No")
                sys.exit()
                
print("Yes")