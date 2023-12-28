n=int(input())
odd_num = sum(1 if int(i) % 2 == 1 else 0 for i in input().split())

if odd_num %2 == 1:
    print("NO")
else:
    print("YES")