n=int(input())
A=list(map(int,input().split()))

ans = "Yes" if len(set(A)) == 1 else "No"
print(ans)