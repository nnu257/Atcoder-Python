n=int(input())

tmp = n 
digit = 0
while tmp > 0:
    tmp -= 5*(4**(digit))
    digit += 1
    
left = tmp + 5*(4**(digit-1))
print()