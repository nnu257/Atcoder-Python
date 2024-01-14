from collections import Counter

n=int(input())
digits = 5

ans = ["0", "2", "4", "6", "8"]
tmps = ["0", "2", "4", "6", "8"]
for i in range(digits):
    arr = tmps[:]
    tmps = [j+tmp for tmp in arr for j in ["2","4","6","8"]]
    ans.extend(tmps)

print(ans[:200])
counts = [len(tmp) for tmp in ans]
counts = Counter(counts)
print(counts.items())
