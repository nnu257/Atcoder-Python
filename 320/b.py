s=input()

subs = [s[j:j+i] for i in range(1,len(s)+1) for j in range(len(s)-i+1)]
subs.sort(key=len, reverse=True)

def check(sub):
    long = len(sub)
    if sub[:long//2] == sub[:long//2-1+(long%2):-1]:
        return True
    return False

for sub in subs:
    if check(sub):
        print(len(sub))
        exit()