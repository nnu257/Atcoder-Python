n=int(input())

judge = False

while n%2==0 or n%3==0:
    if n%2==0:
        n /= 2
    if n%3==0:
        n /= 3

if n == 1.0:
    print("Yes")
else:
    print("No")