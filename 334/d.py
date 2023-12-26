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



n,q = map(int, input().split())
rs = list(map(int, input().split()))
len_rs = len(rs)

rs.sort()

'''
for i in range(q):
    x = int(input())
    
    used_rein = 0
    move_sle = 0
    index = 0
    while True:
        if index <= len_rs-1:
            if used_rein+rs[index] <= x:
                used_rein += rs[index]
                move_sle += 1
                index += 1
            else:
                break
        else:
            break
    print(move_sle)
'''

rs_add = [rs[0]]
for i in range(1, len(rs)):
    rs_add.append(rs_add[i-1]+rs[i])
    
querys = [int(input()) for i in range(q)]
answers = [binary_search(rs_add, x)+1 for x in querys]
print("\n".join([str(x) for x in answers]))

'''
for i in range(q):
    x = int(input())
    print(binary_search(rs_add, x)+1)
'''