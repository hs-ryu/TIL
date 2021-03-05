import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1,T+1):
    N, M = map(int, input().split())
    Paris = []
    max_value = 0
    for i in range(N):
        Paris.append(list(map(int, input().split())))
    for i in range(0, N - M + 1):
        for j in range(0, N - M + 1):
            value = 0
            for k in range(i, i + M):
                for h in range(j, j + M):
                    value += Paris[k][h]
            if value > max_value:
                max_value = value
    print('#{0} {1}'.format(t, max_value))


