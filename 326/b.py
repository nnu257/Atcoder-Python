n=int(input())

for i in range(n, 920):
    tmp = list(str(i))
    if int(tmp[0])*int(tmp[1]) == int(tmp[2]):
        print(i)
        break