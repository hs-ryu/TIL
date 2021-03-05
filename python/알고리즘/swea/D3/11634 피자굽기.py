import sys
sys.stdin = open('sample_input(9).txt')


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    CI = list(map(int, input().split()))
    Q = [i for i in range(N)]
    idx = [i for i in range(N, M)]
    while len(Q) > 1:
        x = Q.pop(0)
        CI[x] //= 2
        if CI[x] == 0:
            if idx:
                i = idx.pop(0)
                Q.append(i)
        else:
            Q.append(x)
    print('#%d %d' % (t, Q[0] + 1))