from itertools import accumulate
n=int(input())
A=list(map(int,input().split()))

acc = list(accumulate(A))
tmp = min(acc)

first = (-1)*tmp if tmp < 0 else 0

print(acc[-1]+first)