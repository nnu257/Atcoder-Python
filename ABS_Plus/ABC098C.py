n=int(input())
s=input()
'''
def my_split(i):
    if i == 0:
        return "", s[1:]
    elif i == n-1:
        return s[:-1], ""
    else:
        return s[:i], s[i+1:]

num = n
for i in range(n):
    left, right = my_split(i)
    tmp = left.count("W")+ right.count("E")
    #print(f"{i}, {left}, {right}, {tmp}")
    num = min(tmp, num)
print(num)
'''
counts = [0 for i in range(n)]
counts[0]=s[1:].count("E")

for i in range(1, n):
    tmp = counts[i-1]
    if s[i] == "E":
        tmp -= 1
    if s[i-1] == "W":
        tmp += 1
    counts[i] = tmp

#print(counts)
print(min(counts))
        