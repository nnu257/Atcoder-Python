k,g,m=map(int, input().split())

glass, mug = 0, 0

for i in range(k):
    
    if glass == g:
        glass =  0
    elif mug == 0:
        mug = m
    else:
        move = min(mug, g-glass)
        glass += move
        mug -= move
        
        
print(f"{glass} {mug}")