n=list(input())

before = "10"
for i in range(len(n)):
    if int(n[i]) >= int(before):
        print("No")
        exit()
    before = n[i]
    

print("Yes")