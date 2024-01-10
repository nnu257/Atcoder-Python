n=int(input())
S=[input() for i in range(n)]

ANS =  [[S[i].count("o"), i] for i in range(n)]

# 優先度の低いユーザーindexでソートしてから，優先度の高い勝利数でソートし直す
ANS.sort(key=lambda x:(x[1]))
ANS.sort(key=lambda x:(x[0]), reverse=True)

ANS = [x[1]+1 for x in ANS]
print(*ANS)