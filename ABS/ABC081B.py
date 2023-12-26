n=int(input())
A=list(map(int,input().split()))

n = 0
while True:
    judge_error = 0
    for i in range(len(A)):
        if A[i] % 2 == 1:
            judge_error = 1
            break
        A[i] /= 2
    
    if judge_error:
        break
    else:
        n += 1
        
print(n)
        