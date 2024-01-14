n=int(input())
A=list(map(int,input().split()))
central = (n+1)//2

# kを固定して，上から見るかもと考えた．しかし，この時点で10^5食う．ループの中で100程度しか処理できない.
# 長さ2*10^5を100程度で判定できない．
#for i in range(int((n+1)/2),0,-1):

# 配列の最小値とそのindexの中央からの距離で求められると思ったが．ピラミッドは配列の中央を中心とする必要はない．
# 例えば，下のプログラムでは1 2 1 2 1の時最大のサイズが1と出るが，これは上記の仮定を付けているから．
if n%2 == 1:
    worst = min(A)
    
    for diff in range(n//2+1):
        if A[central-1+diff] == worst or A[central-1-diff] == worst:
            break
        
    size = diff+1+(worst-1)
    
else:
    Ad = A[1:]
    worst = min(Ad)
    
    for diff in range(n//2+1):
        if Ad[central-1+diff] == worst or Ad[central-1-diff] == worst:
            break
    size1 = diff+1+(worst-1)
      
  
    Ad = A[1:]
    worst = min(Ad)
    
    for diff in range(n//2+1):
        if Ad[central-1+diff] == worst or Ad[central-1-diff] == worst:
            break
    size2 = diff+1+(worst-1)
    
    size = max(size1, size2)
    
print(min(central, size))