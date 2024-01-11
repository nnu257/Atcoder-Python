n=int(input())
s=list(input())

a_index=[i for i in range(n) if s[i]=="A"]

ans = -2
for index in a_index:
    if index+2 <= n-1:
        if s[index+1] == "B":
            if s[index+2] == "C":
                ans = index
                break

print(ans+1)