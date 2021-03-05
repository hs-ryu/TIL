import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T+1):
    N = int(input())
    D = list(map(int, input().split()))
    ans_list = [0] * len(D)
    for i in range(0, len(D)-1):
        ans = 0
        cnt = 0
        for j in range(i+1, len(D)):
            if D[j] >= D[i]:
                cnt += 1
        ans = len(D)-1-i-cnt
        ans_list[i] = ans
    maxV = 0
    for i in ans_list:
        if ans_list[i] > maxV:
            maxV = ans_list[i]
    print('#%d %d' % (t,maxV))

#maxV = 최소치/최소치보다 더 작은 값으로 초기화
#1. for 문을 이용해서 낙차를 구할 위치 지정.(마지막 한개는 제외됨)
#1-1 최대 낙차(ans)
#2. 1에서 지정된 위치에 대해 낙차 구하기.
#2-1. 그 위치 다음 위치부터 끝까지 비교함.
#2-2. 더 낮은 높이로 쌓인 위치 개수 세기(낙차)