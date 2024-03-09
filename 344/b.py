answer=[]
a = input()
while a != "0":
    answer.append(a)
    a = input()
answer.append(a)

print("\n".join(list(reversed(answer))))