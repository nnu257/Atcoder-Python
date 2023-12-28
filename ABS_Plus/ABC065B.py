import sys

n=int(input())
A=[int(input())-1 for i in range(n)]

tmp = 0
'''
Loop = False
pushed = []
while True:
    if tmp in pushed:
        Loop = True
        break
    if tmp == 1:
        break
    pushed.append(tmp)
    tmp = A[tmp]
'''
i = 0
Loop = True
while i < 100001:
    if tmp == 1:
        Loop = False
        break
    tmp = A[tmp]
    i += 1

if not Loop:
   #print(len(pushed))
   print(i)
else:
    print(-1)