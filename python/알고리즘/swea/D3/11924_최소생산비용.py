import sys
sys.stdin = open('5209_input.txt')


def check(idx, s):
    global min_v
    if idx >= N:
        if s <= min_v:
            min_v = s
        return
    if s > min_v:
        return

    for i in range(N):
        if flag[i] == 0:
            flag[i] = 1
            check(idx+1, s+V[idx][i])
            flag[i] = 0


T = int(input())
for t in range(1, T+1):
    N = int(input())
    V = [list(map(int,input().split())) for _ in range(N)]
    flag = [0] * N
    min_v = 99 * 15 * 15
    check(0,0)
    print('#%d %d' %(t, min_v))


# 교수님

def func(level, cost): # level - 제품번호
    if level >= N:
        min_cost = min(mincost,cost)
        return

    for x in range(N): # x - 공장번호
        if visit[x] != 1:
            visit[x] = 1
            func(level+1, cost+A[level][x])
            visit[x] = 0