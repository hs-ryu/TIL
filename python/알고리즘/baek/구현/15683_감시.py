n, m = map(int,input().split())


office = []
for _ in range(n):
    office.append(list(map(int,input().split())))


cctvs = []
for i in range(n):
    for j in range(m):
        if office[i][j] != 0 and office[i][j] != 6:
            cctvs.append([i,j,office[i][j]])