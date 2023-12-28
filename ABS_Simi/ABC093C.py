inp=list(map(int,input().split()))
inp.sort()
a,b,c=inp

num = 0

tmp = (c-a)//2
num += tmp
a += 2*tmp

tmp = (c-b)//2
num += tmp
b += 2*tmp


tmp_list = [a,b,c]
if a==b and b==c:
    print(num)
elif (a+b+c) % 2 == 0:
    if tmp_list.count(max(tmp_list)) == 1:
        print(num+1)
    else:
        print(num+2)
else:
    if tmp_list.count(max(tmp_list)) == 1:
        print(num+1)
    else:
        print(num+2)