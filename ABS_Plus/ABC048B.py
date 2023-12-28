a,b,x=map(int,input().split())

print(((b-a)/x + (1 if a%x==0 else 0))//1000000000)
print(((b-a)/x + (1 if a%x==0 else 0))%1000000000)

print((b-a)/x%1000000000)

print(b // x - (a - 1) // x)