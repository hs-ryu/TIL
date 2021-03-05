import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T+1):
    N = int(input())
    D = list(map(int, input().split()))
    for i in range(len(D)-1):
        for j in range(i+1, len(D)):
            if D[i] > D[j]:
                D[i], D[j] = D[j], D[i]
    str_list = list(map(str, D))
    result = ' '.join(str_list)
    print('#%d %s' %(t, result))