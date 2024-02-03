h,w,n=map(int,input().split())
G = [["." for j in range(w)] for i in range(h)]


def progress(now_h, now_w, dir):
    if dir == 0:
        now_h = (now_h-1)%h
    elif dir == 1:
        now_w = (now_w+1)%w
    elif dir == 2:
        now_h = (now_h+1)%h
    else:
        now_w = (now_w-1)%w
        
    return now_h, now_w
        
def rotate(dir):
    return (dir+1)%4

def rotate_rev(dir):
    return (dir-1)%4

def action(now_h, now_w, dir):
    if G[now_h][now_w] == ".":
        G[now_h][now_w] = "#"
        dir = rotate(dir)

    else:
        G[now_h][now_w] = "."
        dir = rotate_rev(dir)
        
    now_h, now_w = progress(now_h, now_w, dir)
    return now_h, now_w, dir


now_h, now_w, dir = 0,0,0
# dirは上，右，下，左の順に0,1,2,3とする
for i in range(n):
    now_h, now_w, dir = action(now_h, now_w, dir)
    #print(now_h, now_w, dir)
    
    
for i in range(h):
    print("".join(G[i]))