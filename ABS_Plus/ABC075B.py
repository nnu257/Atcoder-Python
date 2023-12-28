h,w=map(int,input().split())
S = [["*" for i in range(w+2)]]
S.extend(list(input()) for i in range(h))
S.extend([["*" for i in range(w+2)]])

#print(S)
for i in range(1,len(S)-1):
    #print(S[i])
    S[i].insert(0,"*")
    S[i].append("*")


for i in range(1, h+1):
    for j in range(1, w+1):
        #print(f"{i} {j}")
        if S[i][j] == ".":
            bomb = 0
            for k in range(i-1, i+2):
                for l in range(j-1, j+2):
                    #print(f"{k} {l}")
                    if S[k][l] == "#":
                        bomb += 1
            S[i][j] = bomb

for i in range(1,h+1):
    for j in range(1,w+1):
        print(S[i][j], end="")
    print("")  