a,m,l,r=map(int, input().split())

if l <= a <= r:
    right = (r-a)//m
    left = (a-l)//m
    print(right+left+1)
    
elif a < l:
    atol = (l-a)//m+1
    ator = (r-a)//m+1
    
    if (l-a) % m == 0:
        print(ator-atol+1)
    else:
        print(ator-atol)
    
else:
    ltoa = (a-l)//m+1
    rtoa = (a-r)//m+1
    
    if (a-r) % m == 0:
        print(ltoa-rtoa+1)
    else:
        print(ltoa-rtoa)