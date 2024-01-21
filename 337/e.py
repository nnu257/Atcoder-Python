n=int(input())
m=n-1
print(m, flush=True)

for i in range(m):
    print(f"1 {i+1}", flush=True)
    
s=input()
if "1" in s:
    print(s.index("1")+1, flush=True)
else:
    print(n, flush=True)