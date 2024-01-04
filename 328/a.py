n,x=map(int,input().split())
S=list(map(int,input().split()))

S = [i for i in S if i <= x]
print(sum(S))