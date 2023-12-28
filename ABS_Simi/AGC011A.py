# 考え方はある程度わかっていたが，解説の考え方は見た．


n,c,k=map(int,input().split())
T=[int(input()) for i in range(n)]

T.sort()

busses = 0
get_on_num = 0
depart_time = 0

for t in T:
    if get_on_num >= c or t > depart_time:
        busses += 1
        get_on_num = 0
        depart_time = t+k
        
    get_on_num += 1
    
    #print(f"{t}, {busses}, {get_on_num}, {depart_time}")
    
print(busses)