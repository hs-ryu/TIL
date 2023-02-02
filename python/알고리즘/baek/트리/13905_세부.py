# 골드 4
# 크러스컬로? 근데 가중치를 최대로?

def findParrent(x):
    while daepyo[x] != x:
        x = daepyo[x]
    return x
def unionParrent(x,y):
    a = findParrent(x)
    b = findParrent(y)
    if a > b:
        daepyo[a] = daepyo[b]
    else:
        daepyo[b] = daepyo[a]


n,m = map(int,input().split())
s,e = map(int,input().split())
ganseons = [list(map(int,input().split())) for _ in range(m)]
ganseons.sort(key=lambda x:x[2], reverse=True)

daepyo = [i for i in range(n+1)]

cnt = 0
i = 0
result = 0

while cnt < n and i < n:
    temp = ganseons[i]
    
    if findParrent(temp[0]) != findParrent(temp[1]):
        result += temp[2]
        unionParrent(temp[0], temp[1])
        cnt += 1
        i += 1
    else:
        i += 1
print(daepyo)
print(result)