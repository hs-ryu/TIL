import sys
sys.stdin = open('ex01input.txt')

T = int(input())
for t in range(1, T+1):
    M = []
    for i in range(5):
        N = list(map(int,input().split()))
        M.append(N)
    dr = [-1,1,0,0]
    dc = [0,0,1,-1]
    s = 0
    for i in range(len(M)):
        for j in range(len(N)):
            for k in range(len(dr)):
                x = i + dr[k]
                y = j + dc[k]
                if x < 0 or x > len(M)-1 or y<0 or y > len(M)-1:
                    continue
                k = M[x][y] - M[i][j]
                if k < 0:
                    # k = -k    요게 더 성능 좋다.
                    k *= (-1)
                s += k
    print('#%d %d'%(t,s))




