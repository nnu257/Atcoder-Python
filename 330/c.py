import math

d=int(input())

route = math.ceil(math.sqrt(d))

# x<=yとしても一般性を失わない
# yのループ
tmp_d = d
for i in range(1, route+1):
    left = d-i**2
    if left <= 0:
        tmp_d = min(tmp_d, abs(left))
    else:    
        # x = ceil(sqrt(D-y^2))とし，-1も調べれば十分
        x = math.ceil(math.sqrt(left))
        tmp_d = min(tmp_d, min(abs(left-x**2), abs(left-(x-1)**2)))
    
print(tmp_d)