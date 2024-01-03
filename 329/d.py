n,m=map(int,input().split())
A=list(map(int, input().split()))

# 1次元のリストは[:]で深いコピー，二次元はimport copy, copy.deepcopy()
# 一次元でも=だと浅い．
'''
Cs = [[0 for i in range(n+1)] for j in range(m)]
Cs[0][A[0]-1] = 1
Cs[0][-1] = A[0]-1
for i in range(1,m):
    a = A[i]
    
    # 表のカウントアップ
    Cs[i] = Cs[i-1][:]
    Cs[i][a-1] += 1
    
    max_ind = Cs[i][-1]
    
    # maxの要素取得
    if Cs[i][a-1] > Cs[i][max_ind]:
        Cs[i][-1] = a-1
    if Cs[i][a-1] == Cs[i][max_ind]:
        Cs[i][-1] = min(a-1, max_ind)
'''
#print(Cs)


Elected = [-1 for i in range(m)]
Elected[0] = A[0]-1

elect = [0 for i in range(n)]
elect[A[0]-1] = 1

#print(f"{0}:{Elected}")

for i in range(1,m):
    a_ind = A[i]-1
    
    elect[a_ind] += 1
    max_ind = Elected[i-1]
    
    if elect[a_ind] > elect[max_ind]:
        Elected[i] = a_ind
    elif elect[a_ind] == elect[max_ind]:
        Elected[i] = min(a_ind, max_ind)
    else:
        Elected[i] = max_ind
            
    #print(f"{i}:{Elected}")

print("\n".join([str(x+1) for x in Elected]))