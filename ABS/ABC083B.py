n,a,b=map(int, input().split())
add=0

for i in range(1,n+1):
    tmp = sum([int(j) for j in str(i)])
    
    if a <= tmp <= b:
        add += i
        
print(add)