import sys
sys.stdin = open('sample_input_minmax.txt')

def minmaxgap(arg):
    maxV = 0
    for num in arg:
        if num > maxV:
            maxV = num
    minV = maxV
    for num in arg:
        if num < minV:
            minV = num
    return maxV-minV

T = int(input())
for t in range(1, T+1):
    N = int(input())
    D = list(map(int, input().split()))
    print('#%d %d' %(t, minmaxgap(D)))
