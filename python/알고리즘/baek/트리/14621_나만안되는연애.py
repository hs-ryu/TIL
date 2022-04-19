def find_daepyo(x):
    while daepyo[x] != x:
        x = daepyo[x]
    return x


n, m = map(int,input().split())
university = [0] + list(input().split())
daepyo = list(range(n+1))
# u,v,d
ganseons = [list(map(int,input().split())) for _ in range(m)]
ganseons.sort(key=lambda x:x[2])
# print(ganseons)

cnt = 0
i = 0
result = 0

# 크러스컬
while cnt < m and i < m:
    temp = ganseons[i]
    # 서로 성별이 다른 대학일때만 체크
    if find_daepyo(temp[0]) != find_daepyo(temp[1]) and university[temp[0]] != university[temp[1]]:
        result += temp[2]
        # union해주기
        daepyo[find_daepyo(temp[0])] = find_daepyo(temp[1])
        cnt += 1
    i += 1

if cnt != n-1:
    result = -1
print(result)