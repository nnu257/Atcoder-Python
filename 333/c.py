n=int(input())

digit = 12

def same(a,b):
    if a==b:
        return 1
    else:
        return 0

digits = sorted(list(set(["" .join([str(same(x,i)+same(x,j)+same(x,k)) for x in range(digit)]) for k in range(digit) for j in range(digit) for i in range(digit)])))
n_num = list(digits[n-1])
#print(digits)

repunits = list(reversed(["1"*y for y in range(1,digit+1)]))

#print(n_num)
#print(repunits)

answer = 0
for i in range(digit):
    answer += int(n_num[i])*int(repunits[i])
print(answer)