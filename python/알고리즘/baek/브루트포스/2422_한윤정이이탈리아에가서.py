n,m = map(int,input().split())
info = dict()
for i in range(1,n+1):
    info[i] = set()

result = 0
for i in range(m):
    a,b = map(int,input().split())
    info[a].add(b)
    info[b].add(a)

for i in range(1,n-1):
    for j in range(i+1,n):
        for k in range(j+1,n+1):
            if (j in info[i] or k in info[i]) or (i in info[j] or k in info[j]) or (i in info[k] or j in info[k]):
                continue
            result += 1
print(result)