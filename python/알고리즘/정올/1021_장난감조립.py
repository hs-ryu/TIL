
def assemble(i):
    if basic[i] != -1:
        basic[i] += 1
        return
    for j in range(1, n+1):
        if partnum[i][j] != 0:
            for k in range(partnum[i][j]):
                assemble(j)

n = int(input())
m = int(input())

basic = [0] * (n+1)
partnum = [[0] * (n+1) for _ in range(n+1)]
for i in range(m):
    x,y,z = map(int, input().split())
    partnum[x][y] = z
    basic[x] = -1
assemble(n)
for i in range(1,n+1):
    if basic[i] != -1:
        print(i, basic[i])