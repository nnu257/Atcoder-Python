a,b,c,d=[int(i) for i in list(input())]

def calc(flag, x, y):
    if flag == 0:
        return x+y
    else:
        return x-y
    
def change(flag):
    if flag == 0:
        return "+"
    else:
        return "-"

judge = False
for i in range(2):
    for j in range(2):
        for k in range(2):
            if calc(k, calc(j, calc(i,a,b), c), d) == 7:
                judge = True
                break
        if judge:
            break
    if judge:
        break   
            
print(f"{a}{change(i)}{b}{change(j)}{c}{change(k)}{d}=7")