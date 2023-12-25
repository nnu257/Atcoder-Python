n,m=map(int, input().split())
s = input()

ss = s.split("0")

need = 0
'''
for x in ss:
    eat = x.count("1")
    pro = x.count("2")
    
    tmp = 0
    while True:
        if tmp == pro+max(0, (eat-n-tmp)):
            if tmp > need:
                need = tmp
            break
        else:
            tmp += 1
'''

for x in ss:
    eat = x.count("1")
    pro = x.count("2")
    len = eat+pro
    
    need = max(need, max(len-m, pro))


print(need)