from itertools import accumulate
from bisect import bisect_left

n,m=map(int,input().split())
A=list(map(int,input().split()))

def binary_search(data, value):
    left = 0            # 探索する範囲の左端を設定
    right = len(data) - 1            # 探索する範囲の右端を設定
    while left <= right:
        judge_move = 0
        mid = (left + right) // 2            # 探索する範囲の中央を計算
        if data[mid] == value:
            # 中央の値と一致した場合は位置を返す
            return mid
        elif data[mid] < value:
            # 中央の値より大きい場合は探索範囲の左を変える
            left = mid + 1
            judge_move = 1
        else:
            # 中央の値より小さい場合は探索範囲の右を変える
            right = mid - 1
            judge_move = 2
     
    if judge_move == 1:
        return right
    else:
        return left-1

A.sort()

#print(A)

ans=0
for i in range(n):
    #tmp = binary_search(A, A[i]+m)-i+1
    tmp = bisect_left(A, A[i]+m)-i
    #print(f"{i}, {A[i]}, {A[i]+m}, {tmp}")
    ans = max(tmp, ans)
    
print(ans)