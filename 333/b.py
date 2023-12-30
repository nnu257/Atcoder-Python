S1,S2=list(input())
T1,T2=list(input())

def change(x):
    if x == "A":
        return 0
    elif x == "B":
        return 1
    elif x == "C":
        return 2
    elif x == "D":
        return 3
    elif x == "E":
        return 4
    
S1,S2,T1,T2=change(S1),change(S2),change(T1),change(T2)

def distance(a,b):
    tmpa,tmpb,tmpds = a,b,0
    while tmpa != tmpb:
        tmpa += 1
        tmpa %= 5
        tmpds += 1
    return tmpds

def distance_rev(a,b):
    tmpa,tmpb,tmpds = a,b,0
    while tmpa != tmpb:
        tmpa += 4
        tmpa %= 5
        tmpds += 1
    return tmpds

ds = min(distance(S1,S2), distance_rev(S1,S2))
dt = min(distance(T1,T2), distance_rev(T1,T2))

if ds == dt:
    print("Yes")
else:
    print("No")