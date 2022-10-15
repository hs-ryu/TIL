# 32점

# 오른쪽이나 아래로만 움직인다 -> 최단경로?
# 1부터 o 표시가 있는 점까지 가는 최단경로 + o 표시에서 끝까지 갈 수 있는 최단경로 => 답

n,m,k = map(int,input().split())

# 4 x 3 배열에서, 최단경로 개수? -> 7! / (4! * 3!)
# k 위치는 한번 거쳐야 하니까. k 위치에 대한 좌표를 먼저 구하고
# r,c에 대해 0,0 -> r,c 까지 가는 최단 경로 + r,c 에서 n,m 까지 가는 최단 경로
if k != 0:

    r = k // m
    c = (k-1) % m

    factorial_r = 1
    factorial_c = 1
    factorial_rc = 1
    for i in range(1,r+1):
        factorial_r *= i
    for i in range(1,c+1):
        factorial_c *= i
    for i in range(1,r+c+1):
        factorial_rc *= i
    route1 = factorial_rc // (factorial_r * factorial_c)

    factorial_r = 1
    factorial_c = 1
    factorial_rc = 1
    for i in range(1,n-r):
        factorial_r *= i
    for i in range(1,m-c):
        factorial_c *= i
    for i in range(1, n-r+m-c-1):
        factorial_rc *= i

    route2 = factorial_rc // (factorial_r * factorial_c)
    print(route1 * route2)
else:
    factorial_r = 1
    factorial_c = 1
    factorial_rc = 1
    for i in range(1,n):
        factorial_r *= i
    for i in range(1,m):
        factorial_c *= i
    for i in range(1, n+m-1):
        factorial_rc *= i
    route = factorial_rc // (factorial_r * factorial_c)
    print(route)