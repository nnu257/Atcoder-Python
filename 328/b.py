n=int(input())
D=list(map(int,input().split()))

num = 0
for i in range(1,n+1):
    for j in range(1,D[i-1]+1):
        date = list(str(i)+str(j))
        if len(set(date))==1:
            num += 1
            
print(num)
        