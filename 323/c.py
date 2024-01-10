n,m=map(int,input().split())
A=list(map(int,input().split()))
S=[list(input()) for i in range(n)]

def change(chara):
    if chara == "o":
        return 1
    else:
        return 0

scores = [0]*n
for i in range(n):
    situation = S[i]
    scores[i] = sum([change(situation[j])*A[j] for j in range(m)])+(i+1)

one = max(scores) 
one_index = scores.index(one)
one_count = scores.count(one)

needed = [one-scores[i]+1 if (one_count!=1 or i!=one_index) else 0 for i in range(n)]

#print(*needed)

A=[(A[i], i) for i in range(m)]
A.sort(key=lambda x:x[0], reverse=True)


ans = [0]*n
for i in range(n):
    
    need = 0
    num = 0
    while needed[i] > 0:
        if S[i][A[num][1]]=="x":
            needed[i]-=A[num][0]
            need += 1
        num += 1
    ans[i] = need


print(*ans)