import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for t in range(1, T+1):
    N = int(input())
    cards = list(map(int,input()))
    print(cards)
    max_cnt_num = 0
    max_cnt = 1
    for i in range(len(cards)-1):
        cnt = 1
        for j in range(i+1, len(cards)):
            if cards[i] == cards[j]:
                cnt += 1
            if cnt > max_cnt:
                max_cnt = cnt
                max_cnt_num = cards[i]
    if max_cnt == 1:
        max_num = 0
        for k in range(len(cards)):
            if cards[k] > max_num:
                max_num = cards[k]
        print('#%d %d %d' % (t, max_num, max_cnt))
    else:
        print('#%d %d %d' % (t, max_cnt_num, max_cnt))