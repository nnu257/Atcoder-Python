from collections import Counter
c=list(Counter(list(input())).items())

c.sort(key=lambda x:x[0], reverse=False)
c.sort(key=lambda x:x[1], reverse=True)

print(c[0][0])