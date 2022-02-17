
# 백트래킹
def search(k):
    # 다 확인했다? 딥 1 증가
    if k == n * m:
        global answer
        answer += 1
        return

    # 현재 좌표
    x = k % m
    y = k // m

    # 좌표가 범위내에 있는 경우
    # 위,왼,위왼 위치에 네모가 있으면 바로 다음칸 확인
    if (0 < y < n and 0 < x < m) and (arr[y-1][x] and arr[y][x-1] and arr[y-1][x-1]):
        search(k + 1)
    # 네모가 없는 경우
    else:
        # 네모 추가한 경우 체크
        arr[y][x] = 1
        search(k+1)
        # 네모 추가하지 않은 경우 체크
        arr[y][x] = 0
        search(k+1)

n,m = map(int,input().split())
arr = [[0 for _ in range(m)] for _ in range(n)]

answer = 0
search(0)
print(answer)