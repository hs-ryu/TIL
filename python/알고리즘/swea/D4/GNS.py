# 정렬문제...
# 1. 카운팅 정렬 사용해보기.
# 2. 수업에서 배운 특별한 정렬 사용해보기.

import sys
sys.stdin = open('GNS_test_input.txt')

# def counting_sort():

num = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
T = int(input())
for t in range(1,T+1):
    length = int(input().split()[1])
    arr = list(input().split())
    cnt = [0 for i in range(len(num))]
    result = [0 for i in range(len(arr))]
    # 카운팅 정렬 사용. 1차 제출
    for i in range(len(arr)):
        cnt[num.index(arr[i])] += 1
    for i in range(1, len(cnt)):
        cnt[i] += cnt[i-1]
    for i in range(len(result)-1, -1, -1):
        result[cnt[num.index(arr[i])]-1] = num[num.index(arr[i])]
        cnt[num.index(arr[i])] -= 1
    print('#%d' %t)
    print(*result)
