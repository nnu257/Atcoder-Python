n,l=map(int,input().split())
A=list(map(int,input().split()))

print(sum([1 if x>=l else 0 for x in A]))