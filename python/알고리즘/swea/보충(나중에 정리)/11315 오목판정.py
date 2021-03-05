import sys
sys.stdin = open('sample_input2.txt')























'''

def chk(row, col):
    dr = [0, 1, 1, 1]
    dc = [1, 0, -1, 1]
    #가로 체크
    cnt = 0
    idxr = row
    idxc = col
    for i in range(4):
    while chk[idxr][idxc] == 'o'
        idxr += dr[i]
        idxc += dc[i]
        if cnt==5:
            return True
    return False
T = int(input())
for t in range(1, T+1):
    N = int(input())
    BRD = [input() for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if BRD[i][j] == 'o':
                ischk = chk(i,j)
                if ischk:
                    break
        if ischk:
            break
    print('#%d %s' % (t, ischk))
'''