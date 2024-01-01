from math import ceil

n,s,m,l=map(int,input().split())

l_num = ceil(n/12)
m_num = ceil(n/8)
s_num = ceil(n/6)

tmp = 1e10
for i in range(s_num+1):
    for j in range(m_num+1):
        for k in range(l_num+1):
            if i*6+j*8+k*12 >= n:
                if i*s+j*m+k*l < tmp:
                    tmp = i*s+j*m+k*l
                    
print(tmp)