import sys
n=int(input())
infos=[list(map(int,input().split())) for i in range(n)]

tmp_h = max([x[2] for x in infos])
while True:
    for tmp_cx in range(101):
        for tmp_cy in range(101):
            judge = True
            for info in infos:
                if info[2] != max(tmp_h-abs(info[0]-tmp_cx)-abs(info[1]-tmp_cy), 0):
                    judge = False
                    break
                
            if judge:
                print(f"{tmp_cx} {tmp_cy} {tmp_h}")
                sys.exit()
            
    tmp_h += 1