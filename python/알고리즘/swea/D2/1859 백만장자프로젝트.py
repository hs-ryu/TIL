import sys
sys.stdin = open('input3.txt')

T = int(input())
for t in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    answer = 0
    maxV = lst[-1]
    for i in range(len(lst)-1, -1, -1):
        if lst[i] > maxV:
            maxV = lst[i]
            continue
        answer += maxV - lst[i]
    print('#%d %d' %(t, answer))