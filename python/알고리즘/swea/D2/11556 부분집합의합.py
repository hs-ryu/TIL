import sys
sys.stdin = open('sample_input_sub.txt')

T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    x = 12
    three_over_total_list = []
    for i in range(1<<x+1):
        three_over_list = []
        total = 0
        for j in range(1, x+1):
            if i & (1<<j):
                three_over_list.append(j)
                total += j
        if len(three_over_list) == N and total == K and three_over_list not in three_over_total_list:
            three_over_total_list.append(three_over_list)
    print(three_over_total_list)
    print('#%d %d' % (t, len(three_over_total_list)))



