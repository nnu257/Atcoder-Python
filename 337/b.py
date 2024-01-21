s=list(input())

move="A"
i=0
while i<len(s):
    if s[i] != move:
        if move == "A":
            move = "B"
        elif move == "B":
            move = "C"
        else:
            print("No")
            exit()
    else:  
        i += 1
            
print("Yes")