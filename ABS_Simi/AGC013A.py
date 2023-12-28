n=int(input())
A=list(map(int,input().split()))


change = 1
judge = 0

if len(A) < 3:
    print(len(A))
    # last テストケース→1にしないと！
else:
    up_down = 1 if A[1]-A[0] >= 0 else 2
    for i in range(2, len(A)):
        
        if A[i]-A[i-1] > 0:
            tmp_up_down = 1
        elif A[i]-A[i-1] < 0:
            tmp_up_down = 2
        else:
            tmp_up_down = up_down
        
        if up_down * tmp_up_down == 2:
            change += 1
            up_down = 0
        else:
            up_down = tmp_up_down
            
        #print(f"{i} {up_down} {change}")
    print(change)
    
# →lastのテストケースのみ通らず