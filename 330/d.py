import numpy as np

# かなり固まってきた段階で答えをなんとなく見た．

n=int(input())
S = [list(input()) for i in range(n)]
St = np.array(S).T.tolist()

counts_h = [S[i].count("o") for i in range(n)]
counts_w = [St[i].count("o") for i in range(n)]

num = 0
for i in range(n):
    if counts_h[i]>1:     
        for j in range(n):
            if counts_w[j] > 1:
                if S[i][j] == "o":
                    num += (counts_w[j]-1)*(counts_h[i]-1)
    
print(num)