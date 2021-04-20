import sys
sys.stdin = open('sample_input.txt')

# 상태확인용 변수 사용
# 행, 열, 대각선(좌상), 대각선(우상) 총 4개 상태확인 변수
# 행 = [0] * N     ->   [1,0,0,0]  = 맨 앞에 행은 쓰고 있다 이미    굳이 신경 안써도 될듯
# 열 = [0] * N     ->   [1,0,0,0]  = 맨 앞에 열은 쓰고 있다 이미    ->   체크하면서 1이면 그 열에 못놓는다!   v0[c] = 1
# 대각은 우째짤까?
# 대각선 [0] * (2*N -1)(좌상) [0,0,0,1,0,0,0]  v1[r-c+(N-1)] = 1
# 대각선 (우상) [0,0,0,1,0,0,0]  v2[r+c] = 1

'''
for c in range(N):
    if v0[c] or v1[r-c+n] or v2[r+c] : continue
    if not v0[c] and not v1[r-c+n] and not v2[r+c]:
        v0[c] = 1
        v1[r-c+n] = 1
        v2[r+c] = 1
        Function(r+1)
        v0[c] = 0
        v1[r-c+n] = 0
        v2[r+c] = 0
'''

def queen(r):
    if r >= N:
        global cnt
        cnt += 1
        return

    for c in range(N):
        if v0[c] or v1[r-c+(N-1)] or v2[r+c]:
            continue
        v0[c] = 1
        v1[r-c+(N-1)] = 1
        v2[r+c] = 1
        queen(r+1)
        v0[c] = 0
        v1[r-c+(N-1)] = 0
        v2[r+c] = 0



T = int(input())
for t in range(1, T+1):
    N = int(input())
    v0 = [0] * N
    v1 = [0] * (2 * N -1)
    v2 = [0] * (2 * N -1)
    cnt = 0
    queen(0)
    print('#%d %d' %(t, cnt))