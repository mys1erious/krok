n = 3
a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
s_1 = {i for i in range(n)}
s_2 = {i for i in range(n)}

ans = 0
t1 = 0

for i in a:
    if t1 in s_1:
        t2 = 0
        for j in i:
            if t2 in s_2:
                ans+=a[t1][t2]
            t2+=1
    t1+=1

print(ans)