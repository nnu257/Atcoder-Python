from itertools import accumulate
from collections import Counter

n=int(input())
A=list(map(int,input().split()))
'''
accumulateの知識が足りず，カスタマイズするのではなく帳尻合わせに走ってしまった．40分経過で諦めた．

sorted_A = list(set(sorted(A)))
index_A = [sorted_A.index(x) for x in A]
count_A = sorted(list(Counter(A).items()), key=lambda x:x[0])+[(0,0)]
sums = list(accumulate(set(sorted_A)))
sums_max = sums[-1]

print(sorted_A)
print(index_A)
print(count_A)
print(sums)

than_me = [sums_max-sums[i] for i in range(len(sorted_A))]
than_me_index = [str(than_me[index_A[i]]+(count_A[index_A[i]+1][1]-1)*count_A[index_A[i]+1][0]) for i in range(n)]

print(than_me)
print(" ".join(than_me_index))
'''


'''
累積和は，自分以下の値の和である．
よって，自分より大きい値の和を求める時は，リストを逆順にソートして考える．

# Aとindexをソートする方法でもよい．
sorted_A = list(sorted(A))+[0]
index_A = [sorted_A.index(x) for x in A]
culm_A = [0 for i in range(n+1)]

tmp_sum = 0
before = 0
stack = 0
for i in range(n+1):
    ele = sorted_A[i]
    if before != ele:
        tmp_sum += ele
        tmp_sum += stack
        stack = 0
    else:
        stack += ele
    before = ele
    culm_A[i] = tmp_sum
    
print(sorted_A)
print(index_A)
print(culm_A)
'''


'''
タプルのソートでなぜうまくいくか不明．理解を諦めた．

#sorted_A = list(sorted(A, reverse=True))
#index_A = [sorted_A.index(x) for x in A]

index_and_A = [[A[i], i] for i in range(n)]
sorted_index_and_A = list(sorted(index_and_A, key=lambda x:x[0], reverse=True))
sorted_A = [x[0] for x in sorted_index_and_A]
index_A = [x[1] for x in sorted_index_and_A]

print(index_and_A)
print(sorted_index_and_A)
print(sorted_A)
print(index_A)


culm_A = [0 for i in range(n)]

tmp_sum = 0
before = sorted_A[0]
for i in range(n):
    ele = sorted_A[i]
    
    if before != ele:
        culm_A[i] = tmp_sum
    else:
        culm_A[i] = culm_A[i-1]
        
    tmp_sum += ele
    before = ele


#print(culm_A)

than_me = [str(culm_A[index_A[i]]) for i in range(n)]
print(" ".join(than_me))
'''

from collections import defaultdict

d=defaultdict(list)
for i,a in enumerate(A):
  d[a].append(i)
sorted_d = sorted(d.items(), reverse=True)

ans=[0]*n
s=0
for v,i_list in sorted_d:
    for i in i_list:
        ans[i]=s
    s+=v*len(i_list)

print(*ans)