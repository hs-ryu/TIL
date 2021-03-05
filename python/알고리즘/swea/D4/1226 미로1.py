import sys
sys.stdin = open('input4.txt')

def find_start_point(miro):
    for i in range(16):
        for j in range(16):
            if miro[i][j] == 2:
                sr, sc = i, j
                return sr, sc

def miro_search(sr, sc):
    Queue.append([sr, sc])
    visited[sr][sc] = 1

    while Queue:
        cr, cc = Queue.pop(0)
        for i in range(4):
            r = cr + dr[i]
            c = cc + dc[i]
            if 0 <= r < 16 and 0 <= c < 16 and visited[r][c] == 0 and miro[r][c] != 1:
                if miro[r][c] == 3:
                    return 1
                Queue.append([r,c])
                visited[r][c] = 1
    return 0

#상하좌우
dc = [0, 0, -1, 1]
dr = [-1, 1, 0, 0]
for t in range(1, 11):
    T = int(input())
    miro = [list(map(int, input())) for _ in range(16)]
    sr, sc = find_start_point(miro)
    visited = [[0 for i in range(16)] for i in range(16)]
    Queue = []
    result = miro_search(sr, sc)
    print('#%d %d' %(T, result))


