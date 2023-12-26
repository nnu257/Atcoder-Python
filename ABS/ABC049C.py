import re
import sys

s=input()
last = 0


if s[-5:] == "dream":
    last += 5
elif s[-7:] == "dreamer":
    last += 7
elif s[-5:] == "erase":
    last += 5
elif s[-6:] == "eraser":
    last += 6
else:
    print("NO")
    sys.exit()

while last != len(s):
    if s[-5-last:-last] == "dream":
        last += 5
    elif s[-7-last:-last] == "dreamer":
        last += 7
    elif s[-5-last:-last] == "erase":
        last += 5
    elif s[-6-last:-last] == "eraser":
        last += 6
    else:
        print("NO")
        sys.exit()

print("YES")