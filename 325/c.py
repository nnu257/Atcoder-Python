import numpy as np
from collections import deque

h,w=map(int,input().split())
S=[list(input()) for i in range(h)]

ANS = [[-1 for i in range(w)] for j in range(h)]

def check_s(y, x):
    if (0<= y <= h-1) and (0 <= x <= w-1):
        if S[y][x] == "#":
            return True
        
    return False
  
'''
# これだと．Uの字などに繋がっているものは判定できない．グラフの深さor幅優先探索が必要．  
ind = 1
for y in range(h):
    for x in range(w):
        if S[y][x] == "#":   
            
            judge = False
            for yy, xx in [(y-1,x-1), (y-1,x), (y-1,x+1), (y,x-1)]:
                if check_s(yy, xx) == "#":
                    ANS[y][x] = ANS[yy][xx]
                    judge = True
                    break
                
            if not judge:
                ANS[y][x] = ind
                ind += 1
                
ANS = np.array(ANS)
'''
def not_checked(y, x):
    if (0<= y <= h-1) and (0 <= x <= w-1):
        if ANS[y][x] == -1:
            return True
        
    return False


done = set()

ind = 1
for y in range(h):
    for x in range(w):
        
        # この座標が"#"でかつ探査済みでないなら
        if check_s(y, x) and (y,x) not in done:
            
            queue = deque()
            # 以降のwhile文があるので，追加するのは[y,x]だけ．周りは必要ない．
            queue.append((y, x))
            
            # 幅優先探索，キューとして利用する
            while len(queue)>0:
                yy, xx = queue.popleft()
                
                # ansはindから取るので，ANSは必要ない，
                #ANS[yy][xx] = ind
            
                for tmp in [(yyy, xxx) for yyy, xxx in [(yy-1,xx-1), (yy-1,xx), (yy-1,xx+1), (yy,xx-1), (yy,xx+1), (yy+1,xx-1),(yy+1,xx),(yy+1,xx+1)] if check_s(yyy,xxx) and (yyy,xxx) not in done]:
                    # 追加したときにdoneに入れる．これがnot_checkedではできない.これにより重複がなくなり，かなり速度up
                    done.add(tmp)
                    queue.append(tmp)
            
            ind += 1

# このような実装であれば．maxではなく，indを使えばよい
# ANS = np.array(ANS)
# print(max(0, ANS.max()))
print(max(0, ind-1))

# 探査確認をnot_checkedでやっていた際，mambaforgeでTLEが18, cpythonで14, PyPyで9となった．
# 提出言語も非常に大事．