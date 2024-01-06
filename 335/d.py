n=int(input())

X = [["0" for i in range(n)] for j in range(n)]
X[0][0] = "1"

x=0
y=0

'''
for i in range(2, n**2):
    if y == 0:
        if x != n-1:
            x += 1
        else:
            y += 1
            
    elif y == n-1:
        if x != 0:
            x -= 1
        else:
            y -= 1
            
    elif x == 0:
        if X[y-1][x] == "0":
            y -= 1
    
    elif x == n-1:
        if X[y+1][x] == "0":
            y += 1
    
    elif X[y][x+1] == "0":
        x += 1
    
    elif X[y+1][x] == "0":
        y += 1
    
    elif X[y][x-1] == "0":
        x -= 1
    
    else:
        y -= 1    
        
    X[y][x] = str(i)
'''

def judge(y,x):
    if 0 <= x <= n-1 and 0 <= y <= n-1:
        if X[y][x] == "0":
            return True
    
    return False

'''
for i in range(2, n**2):
    print(f"{y}, {x} ->", end="")
    if judge(y, x+1):
        x += 1
            
    elif judge(y+1, x):
        y += 1
    
    elif judge(y, x-1):
        x -= 1       
         
    else:
        y -= 1
        
    print(f"{y}, {x}")
        
    X[y][x] = str(i)
    
    # これやばい
    for a in X:
        print(*a)
    print()
'''

direction = 0
for i in range(2, n**2):
    
    if direction == 0:
        if judge(y,x+1):
            x += 1
        else:
            direction = 1
            y += 1
            
    elif direction == 1:
        if judge(y+1, x):
            y += 1
        else:
            direction = 2
            x -= 1
            
    elif direction == 2:
        if judge(y, x-1):
            x -= 1
        else:
            direction = 3
            y -= 1
    
    elif direction == 3:
        if judge(y-1, x):
            y -= 1
        else:
            direction = 0
            x += 1
    
    X[y][x] = i


X[int((n+1)/2)-1][int((n+1)/2)-1] = "T"     

for x in X:
    print(*x)
