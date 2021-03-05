import sys
sys.stdin = open('input.txt')

# 가로, 세로 합들 중 최대값을 출력하는 함수
def garo_sero(x):
    max_garo = 0
    max_sero = 0
    for i in range(len(x)):
        total_garo = 0
        total_sero = 0
        for j in range(len(x[0])):
            total_garo += x[i][j]
            total_sero += x[j][i]
        if total_garo > max_garo:
            max_garo = total_garo
        if total_sero > max_sero:
            max_sero = total_sero
    return max_garo if max_garo > max_sero else max_sero

# 대각선 합들 중 최대값을 출력하는 함수
def daegak(x):
    # 왼쪽 위부터 오른쪽 아래까지 대각선
    total_1 = 0
    # 오른쪽 위부터 왼쪽 아래까지 대각선
    total_2 = 0
    for i in range(len(x)):
        total_1 += x[i][i]
        total_2 += x[i][len(x)-1-i]
    if total_1 > total_2:
        return total_1
    else:
        return total_2

for t in range(1, 11):
    T = int(input())
    x_list = []
    for i in range(100):
        x = list(map(int,input().split()))
        x_list.append(x)
    garosero = garo_sero(x_list)
    daegak_max = daegak(x_list)
    # 가로 세로 합의 최대값과 대각선 합의 최대값 중 큰놈을 출력
    if garosero > daegak_max:
        result = garosero
    else:
        result = daegak_max
    print('#%d %d' %(t, result))