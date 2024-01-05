n,m=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))

# 頂点の情報
# -1は未訪問，1はグループ1，0はグループ0
X = [-1 for i in range(n)]

# 二部グラフの判定フラグ
# 深さ優先探索でダメになったらFalseにする
bipartie = True

# 深さ優先探索による判定
for i in range(n):
    
    # 訪問済みなら無視
    if X[i] == -1:
        continue
    
    # 訪問してないなら，この頂点A[i]に書き込むのは0とし，1,0,1,0と深さ優先で書き込む．
    else:
        X[A[i]] = 0
        
        # 次の頂点に書き込む
        X[B[i]] = 1
