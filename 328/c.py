from itertools import accumulate


n,q=map(int,input().split())
s=input()
query=[list(map(int,input().split())) for i in range(q)]


sames = [0 for i in range(n)]
after = ""
for i in range(n-1,-1,-1):
    if s[i] == after:
        sames[i] = 1
    else:
        after = s[i]

sums = list(accumulate(sames))

#print(sames)
#print(sums)

for l, r in query:
    r = sums[r-2] if r!=1 else 0
    l = sums[l-2] if l!=1 else 0
    print(r-l)