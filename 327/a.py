import sys

n=int(input())
s=input()

before = ""
for i in range(n):
    if (before == "a" and s[i] == "b") or (before == "b" and s[i] == "a"):
        print("Yes")
        sys.exit()
    else:
        before = s[i]

print("No")