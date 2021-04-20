import sys
sys.stdin = open('5208_input.txt')

def go_bus(idx, change_bat):
    global min_change

    if change_bat >= min_change:
        return
    if idx >= N:
        if change_bat < min_change:
            min_change = change_bat
        return

    for i in range(M[idx], 0, -1):
        if visit[idx] != 1:
            visit[idx] = 1
            go_bus(idx+i, change_bat+1)
            visit[idx] = 0



T = int(input())
for t in range(1, T+1):
    lst = list(map(int, input().split()))
    N = lst[0]
    M = [0] + lst[1:]
    visit = [0] * N
    min_change = 101
    go_bus(1, 0)
    print('#%d %d' %(t,min_change-1))