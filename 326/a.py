x,y=map(int,input().split())

if x > y:
    if x - y <= 3:
        print("Yes")
    else:
        print("No")
        
if x < y:
    if y - x <= 2:
        print("Yes")
    else:
        print("No")