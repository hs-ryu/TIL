import sys
sys.stdin = open('sample_input_bus.txt')

T = int(input())
for t in range(1, T+1):
    K, N, M = map(int, input().split())
    Battery = list(map(int, input().rstrip().split()))
    count = 0
    temp = 0
    while temp < N-K:
        for j in range(K, 0, -1):
            if temp+j in Battery:
                count += 1
                temp += j
                break
        else:
            count = 0
            break
    print('#%d %d'%(t, count))




