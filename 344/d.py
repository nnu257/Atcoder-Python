from collections import deque

t=input()
len_t=len(t)
n=int(input())
bag = [input().split(" ")[1:] for _ in range(n)]
    
# キュー幅優先探索で計算量が足りそう．append, popleft
# 作っていくのではなく，消していくイメージ．
# キューの要素は，[i(どこのバッグまで使ったか), 現在の文字列, 現在のコスト]
ans = 101
q = deque()
q.append([-1, -1, 0])
while q:
    
    # 取り出し
    i, elased_i, cost = q.pop()
    
    # 文字列が出来上がっていれば，コストを計上し，そのキューは削除
    if elased_i == len_t-1:
        ans = min(ans, cost)
        continue
    
    # 残っていて，最後のかばんまで見ていなければ，次のかばんを見る
    if i!= n-1:
        if cost <= ans-2:
            if len_t-elased_i-1 <= 10*(n-1-i):
            
                for string in bag[i+1]:
                    length = len(string)
                    if t[elased_i+1:elased_i+1+length] == string:
                        q.append([i+1, elased_i+length, cost+1])
                q.append([i+1, elased_i, cost])
        
ans = ans if ans != 101 else -1
print(ans)

# 上記だとTLEになったので幅優先でなく深さ優先とし，コストがその時点でansより大きいものは削除していく．
# つまり，popleftをpopに変え．cost判断を追加する．
# それでもアウト．残りが100文字でカバンが1個しかない場合などはアウトなどで，それも削除
# それもアウト．CPythonで出すとむしろ遅い．
# 残りの文字の持ち方を工夫して，数字にしてもだめ

# 動的計画法らしいけど，意味不明