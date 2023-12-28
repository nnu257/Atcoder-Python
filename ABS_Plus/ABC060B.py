import sys

a,b,c=map(int,input().split())

tmp = a%b
for i in range(b+10):
    tmp += a
    tmp %= b
    if tmp == c:
        print("YES")
        sys.exit()

print("NO")