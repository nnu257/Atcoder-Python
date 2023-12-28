from collections import Counter

n=int(input())
A=[int(input()) for i in range(n)]

'''
written = []
for a in A:
    if a not in written:
        written.append(a)
    else:
        written.remove(a)

print(len(written))
'''

print(len([1 for num, exis in list(Counter(A).items()) if exis % 2 != 0]))
