n=int(input())
QUERY=[list(map(int,input().split())) for i in range(n)]

taka=0
ao=0

for query in QUERY:
    taka += query[0]
    ao += query[1]
    
if taka > ao:
    print("Takahashi")
elif ao > taka:
    print("Aoki")
else:
    print("Draw")