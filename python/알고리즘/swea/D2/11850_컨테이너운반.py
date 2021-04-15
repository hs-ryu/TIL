import sys
sys.stdin = open('5201_input.txt')


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    weights = list(map(int, input().split()))
    volumes = list(map(int, input().split()))
    total_weights = 0
    while weights and volumes:
        highst_weights = weights.pop(weights.index(max(weights)))
        highst_volumes = volumes.pop(volumes.index(max(volumes)))
        if highst_volumes >= highst_weights:
            total_weights += highst_weights
        else:
            volumes.append(highst_volumes)
    print('#%d %d' %(t, total_weights))
