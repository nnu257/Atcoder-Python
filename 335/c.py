from itertools import accumulate

n,q=map(int,input().split())
Q = [input().split() for i in range(q)]

#print("")
# for文中のsumは基本out?

def change(direct):
    if direct == "U":
        return 0,1
    elif direct == "R":
        return 1,0
    elif direct == "D":
        return 0,-1
    else:
        return -1,0

direct_x = []
direct_y = []
needed = []
ind = 0
for query in Q:
    if query[0] == "1":
        ind += 1
        tmp = change(query[1])
        direct_x.append(tmp[0])
        direct_y.append(tmp[1])
    else:
        needed.append([ind, int(query[1])])
   
acc_direct_x = list(accumulate(direct_x))
acc_direct_y = list(accumulate(direct_y))

'''
print(f"needed:{needed}")
print(f"direct_x:{direct_x}")
print(f"direct_y:{direct_y}")
print(f"acc_direct_x:{acc_direct_x}")
print(f"acc_direct_y:{acc_direct_y}")
print("")
'''

for query in needed:
    moved = query[0]
    num = query[1]

    # ここを変えたらACになった．再考
    if moved <= num-1:
        print(f"{num-moved} 0")
    else:
        #print(f"tmp:{moved, num}")
        x = num + (-1)*(num-1) + acc_direct_x[moved-(num-1)-1]
        y = 0 + 0*(num-1) + acc_direct_y[moved-(num-1)-1]
        
        print(f"{x} {y}")
