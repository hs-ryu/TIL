# 유니온


import sys
sys.stdin = open('5248_input.txt')

def find_daepyo(x):
    while x != daepyo[x]:
        x = daepyo[x]
    return x

def union(p1, p2):
    daepyo[find_daepyo(p2)] = find_daepyo(p1)

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    daepyo = list(range(N+1))
    for i in range(M):
        p1,p2 = lst[2*i], lst[2*i + 1]
        union(p1, p2)
    result = 0
    for i in range(1, N+1):
        if daepyo[i] == i:
            result += 1
    print('#%d %d' %(t, result))