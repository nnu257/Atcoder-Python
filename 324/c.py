# 全く解法がわからなかった

n,t=input().split()
#n=int(n)
t = list(t)

S=[list(input()) for i in range(n)]

def check_s(s,t):
    #t=list(t)
    lt, ltd = len(t), len(s)
    len_short = min(lt,ltd)
    
    if not (ltd-1 <= lt <= ltd+1):
        return False
    
    same_f = 0
    same_b = 0
    
    
    for i in range(len_short):
        if s[i]==t[i]:
            same_f += 1
        else:
            break
    
    for i in range(len_short):
        if s[ltd-i-1]==t[lt-i-1]:
            same_b += 1
        else:
            break
    
    
    if same_f == same_b == lt == ltd:
        return True
    elif same_f+same_b == lt-1 == ltd-1:
        return True
    elif same_f+same_b >= lt == ltd-1:
        return True
    elif same_f+same_b >= lt-1 == ltd:
        return True
     
    return False


ans = [i+1 for i in range(n) if check_s(S[i],t)]
print(len(ans))
print(*ans)
    