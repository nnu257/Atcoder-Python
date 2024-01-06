n=int(input())

answer = []
for i in range(n+1):
    for j in range(n+1):
        for k in range(n+1):
            if i+j+k <= n:
                answer.append(" ".join([str(i),str(j),str(k)]))
                
for x in answer:
    print(x)