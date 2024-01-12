k=int(input())

ans_arr = ["0","1","2","3","4","5","6","7","8","9"]
tmp_arr = ["0","1","2","3","4","5","6","7","8","9"]
digit = 100000000


for num in range(digit-1):
    tmp = []
    for x in tmp_arr:
        for i in range(10):
            if i > int(x[0]):
                tmp.append(str(i)+x)
    ans_arr += tmp
    tmp_arr = tmp

ans_arr.sort(key=int)

#print(ans_arr)
print(ans_arr[k])