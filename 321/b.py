n,x=map(int,input().split())
A=list(map(int,input().split()))

for i in range(101):
    tmp = A+[i]
    tmp.sort()
    got=sum(tmp[1:n-1])
    
    #print(i)
    #print(tmp)
    #print(got)
    
    if got >= x:
        print(i)
        exit()
        
print(-1)