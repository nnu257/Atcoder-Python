n,s,k=map(int, input().split())

price = 0

for i in range(n):
    
    p,q=map(int, input().split())

    price += p*q

if price < s:
    price += k
    
print(price)