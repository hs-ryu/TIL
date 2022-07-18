import sys
from pprint import pprint
sys.stdin = open('sample_input.txt')

s = 0

def left_to_right(line):
    global cnt_1
    if line[1]:
        return line
    i = cnt = power = 1
    while i < N:
        if not line[i]:
            line[i-cnt], line[i] = 0, 1
            power *= 1.9
            i += 1
            continue
        j = i
        blocks = 0
        while j < N and line[j]:
            blocks += 1
            j += 1
        if power <= blocks:
            break
        cnt += blocks
        power += blocks
        i += blocks
    return line


for t in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt_1 = 0
    cnt_2 = 0
    for i, line in enumerate(zip(*arr)):
        if line[0]:
            new_line = left_to_right(list(line))
            for j in range(N):
                arr[j][i] = new_line[j]
    for i in range(N):
        if arr[-1][i] == 1:
            cnt_1 += 1
    for i, line in enumerate(arr):
        if line[0]:
            new_line = left_to_right(list(line))
            for j in range(N):
                arr[i][j] = new_line[j]
    for i in range(N):
        if arr[i][N-1] == 1:
            cnt_2 += 1
    print('#%d %d %d' %(t, cnt_1, cnt_2))











# 영주
'''
def get_block_R(row, col):
    block_R = 0
    while row < n and grid[row][col]:
        block_R += 1
        row += 1
    return block_R

def go_down():
    for c in range(n):
        if not grid[0][c] or grid[1][c]:
            continue
        r = count = power = 1
        while r < n:
            if not grid[r][c]:
                grid[r-count][c], grid[r][c] = 0, 1
                power *= 1.9
                r += 1
                continue
            block_R = get_block_R(r, c)
            if power <= block_R:
                break
            count += block_R
            power += block_R
            r += block_R

def swap():
    for i in range(n):
        for j in range(i):
            grid[i][j], grid[j][i] = grid[j][i], grid[i][j]

for t in range(1, 11):
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]
    go_down()
    swap()
    go_down()
    result1 = 0
    for i in range(n):
        result1 += grid[i][-1]
    result2 = sum(grid[-1])
    print('#%s %s %s' % (t, result1, result2))

'''