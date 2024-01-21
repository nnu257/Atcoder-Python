# hとwの制限は十分に小さいので，縦，横の揃える方向を決め撃ちして探索する．
import numpy as np

h,w,k=map(int,input().split())
S=[input() for i in range(h)]
S_l = [list(x) for x in S]
ST_l = np.array(S_l).T.tolist()
ST=["".join(x) for x in ST_l]

#print(S)
#print(ST)

ans = 100000000000000000

def mycount(tmp_notx):
    tmp_list1, tmp_list2 = [0]*len(tmp_notx), [0]*len(tmp_notx)
    sum = 0
    for i in range(len(tmp_notx)):
        if tmp_notx[i] == "o":
            sum += 1
        tmp_list1[i] = sum
    
    for i in range(k-1, len(tmp_notx)):
        if i-k < 0:
            back = 0
        else:
            back = tmp_list1[i-k]
        
        tmp_list2[i] = tmp_list1[i] - back
          
    #print(tmp_list1)
    #print(tmp_list2)
    
    return max(tmp_list2)

# 縦に揃える
for i in range(w):
    tmp = ST[i]
    tmp_max = 0
    judge = False
    for tmp_notx in tmp.split("x"):
        if len(tmp_notx)>=k:
            tmp_max = max(mycount(tmp_notx), tmp_max)
            judge = True
    
    if judge:
        if k < tmp_max:
            ans = 0
        else:
            ans = min(k-tmp_max, ans)
            
# 横に揃える
for i in range(h):
    tmp = S[i]
    tmp_max = 0
    judge = False
    for tmp_notx in tmp.split("x"):
        if len(tmp_notx)>=k:
            tmp_max = max(mycount(tmp_notx), tmp_max)
            judge = True
    
    if judge:
        if k < tmp_max:      
            ans = 0
        else:          
            ans = min(k-tmp_max, ans)
    
    

if ans == 100000000000000000:
    ans = -1
print(ans)