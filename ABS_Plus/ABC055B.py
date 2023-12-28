n=int(input())

power = 1
for i in range(n):
    power *= (i+1)
    power %= 1e9+7
    
print(int(power))