import sys
sys.stdin = open('input10.txt')


# n = 순열 돌릴 개수
# k = 몇번 바꿨는지
def permu(n, k):
    global result
    if k == n:
        start = area[1][manage_list[0]]
        end = area[manage_list[-1]][1]
        middle = 0
        for i in range(len(manage_list)-1):
            middle += area[manage_list[i]][manage_list[i+1]]
        total_battery = start + end + middle
        if total_battery < result:
            result = total_battery

    for i in range(k, n):
        manage_list[k], manage_list[i] = manage_list[i], manage_list[k]
        permu(n, k+1)
        manage_list[k], manage_list[i] = manage_list[i], manage_list[k]


T = int(input())
for t in range(1, T+1):
    N = int(input())
    area = [[0] + list(map(int, input().split())) for _ in range(N)]
    area.insert(0, [0] * (N+1))
    manage_list = [i for i in range(2, N+1)]
    # 순열로 줄 세우기
    result = 10000
    permu(N-1, 0)
    print('#%d %d' %(t, result))