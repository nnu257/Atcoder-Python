n=int(input())
s=list(input())

before = "dummy"
count = 0
counts = []
for i in range(n):
    if s[i] == before:
        count += 1
    else:
        counts.append([before, count])
        count = 1
        before = s[i]
counts.append([before, count])
counts = counts[1:]

counts.sort(key=lambda x:x[1], reverse=True)

looked = []
ans = 0
for key, num in counts:
    if key not in looked:
        looked.append(key)
        ans += num

#print(counts)
print(ans)