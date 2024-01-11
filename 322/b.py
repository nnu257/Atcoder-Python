import re

n,m=map(int,input().split())
s,t=input(),input()

prefix, suffix = False, False
if re.match(s,t):
    prefix=True
if re.search(s+"$",t):
    suffix=True
    
if prefix:
    if suffix:
        print(0)
    else:
        print(1)
else:
    if suffix:
        print(2)
    else:
        print(3)