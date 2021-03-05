import sys
sys.stdin = open('sample_input_sum_1.txt')

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    num_list = list(map(int, input().split()))
    maxV = num_list[0]
    minV = 0
    for i in num_list:
        minV += i
    for i in range(len(num_list)-M+1):
        gugan_hab = 0
        # 슬라이싱 쓰는거 보다 그냥 각 성분으로 for문 돌릴수도 있을듯.
        for j in num_list[i:i+M]:
            gugan_hab += j
        if gugan_hab > maxV:
            maxV = gugan_hab
        if gugan_hab < minV:
            minV = gugan_hab
    print('#%d %d'%(t, maxV - minV))