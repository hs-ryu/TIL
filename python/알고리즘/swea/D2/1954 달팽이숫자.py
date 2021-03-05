# 좌표 이동을 사용해서 풀어보기.
# N * N 행렬은, 총 N * 2 - 1번 반복이 진행된다.
# 인덱스가 홀수일때 이동 숫자가 1씩 줄어든다.
# 우,하,좌,상 순서.
# 만약 좌표이동을 사용하지 않는다고 했을때는 Switch라는 변수 하나를 사용해 우,하,좌(-Switch),상(-Switch) 순환하며 숫자를 채울 수 있다.

T = int(input())
for t in range(1, T+1):
    N = int(input())
    result = [[1 for x in range(1,N+1)] for x in range(N)]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    # fst : 7번(idx) 반복문
    # sec : 4번 반복문
    # trd : x,y증가 반복문
    # 4th : 2번 끝나면 idx + 1,해서 idx가 홀수면 1번을 -1해서 다시 반복
    z = 2
    cnt = N-1
    x, y = 0, 0
    idx = 0
    # 1번 반복문 good!
    while idx < (N * 2 - 1):
        # 3번 반복문 good!
        for delta in range(len(dx)):
            # 2번 반복문 good!
            for _ in range(cnt):
                x += dx[delta]
                y += dy[delta]
                result[x][y] = z
                z += 1
            idx += 1
            if idx == (N * 2 - 1):
                break
            if idx > 2 and idx % 2:
                cnt -= 1
    print('#%d'%t)
    for i in result:
        print(*i)


