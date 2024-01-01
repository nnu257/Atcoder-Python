def send(input, max, min):
    if input == max:
        return min
    else:
        return input+1
    
M,D=map(int,input().split())
y,m,d=map(int,input().split())

if d == D:
    d = 1
    up2 = 1
else:
    d += 1
    up2 = 0
    
up1 = 0
if up2:
    if m == M:
        m = 1
        up1 = 1
    else:
        m += 1
        up1 = 0

if up1:
    y += 1 

print(f"{y} {m} {d}")