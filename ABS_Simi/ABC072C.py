# 1WA, TLEになったが，テストケースが確認できないため理由は不明．
# 考え方の方向性はあっていた．



from collections import Counter
import pandas as pd

n=int(input())
A=list(map(int,input().split()))

c = sorted(list(Counter(A).items()), key=lambda x:x[0])
nums = [x[0] for x in c]
counts = [x[1] for x in c]
maxnum = nums[-1]

new_counts = [counts[nums.index(i)] if i in nums else 0 for i in range(maxnum+1)]
df_count = pd.DataFrame(new_counts)
conv = df_count + df_count.shift(1).fillna(0) + df_count.shift(-1).fillna(0)
#print(new_counts)
#print(conv)

#conv = [(counts[nums.index(i-1)] if i-1 in nums else 0)+(counts[nums.index(i)] if i in nums else 0)+(counts[nums.index(i+1)] if i+1 in nums else 0) for i in range(maxnum+1)]

if len(A) <= 3:
    print(len(A))
else:
    print(int(conv.max()))