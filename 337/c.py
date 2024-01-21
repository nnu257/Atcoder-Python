n=int(input())
A=[[int(x), i+1] for i,x in enumerate(input().split())]
#print(A)

'''
ループn*index nなのでn^2
tmp=A.index(-1)+1

print(tmp, end=" ")
for i in range(n-1):
    tmp=A.index(tmp)+1
    print(tmp,end=" ")
'''

# 辞書型なら，発見はO(1)なのでは？
dic = dict(A)
#print(dic)

tmp = -1
for i in range(n):
    tmp=dic[tmp]
    print(tmp)