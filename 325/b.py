n=int(input())
QUERY=[list(map(int,input().split())) for i in range(n)]

ans = 0
for i in range(24):
    tmp = 0
    for query in QUERY:
        if 9 <= (query[1]+i)%24 <= 17:
            tmp += query[0]
            
    ans = max(ans, tmp)
    
print(ans)