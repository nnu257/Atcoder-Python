import time

a,b,c,d=map(int,input().split())

if b<=c or d<=a:
    print(0)
elif a <= c <= b <= d:
    print(b-c)
elif c <= a <= b <= d:
    print(b-a)
elif c <= a <= d <= b:
    print(d-a)
elif a <= c <= d <= b:
    print(d-c)
else:
    time.sleep(3)