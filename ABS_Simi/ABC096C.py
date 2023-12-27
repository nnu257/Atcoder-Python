a,b,c,x,y=map(int,input().split())

yen = 0
if x >= y:
    same = y
    
    if same*a+same*b > same*2*c:
        yen += same*2*c
    else:
        yen += same*a+same*b
        
    xnew = x-y
    
    if xnew*a > xnew*2*c:
        yen += xnew*2*c
    else:
        yen += xnew*a
        
    print(yen)

else:
    same = x
    
    if same*a+same*b > same*2*c:
        yen += same*2*c
    else:
        yen += same*a+same*b
        
    ynew = y-x
    
    if ynew*b > ynew*2*c:
        yen += ynew*2*c
    else:
        yen += ynew*b
        
    print(yen)