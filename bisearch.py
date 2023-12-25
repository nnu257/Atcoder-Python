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

data = [0,1, 3, 4, 6, 8, 9,12,16,19,23,24,27,29,123,234,456,567,1000]
print(binary_search(data, 13))
print(binary_search(data, 45))