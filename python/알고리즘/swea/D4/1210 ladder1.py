import sys
sys.stdin = open('input3.txt')

# 사다리 타는 함수
def sadari(data, start_idx):
    # 각 시작 위치부터 하나씩 반복
    for start in start_idx:
        x = start
        y = 1
        direction = ''
        # 끝까지 도달할때 까지 반복
        while y < len(data)-1:
            # 오른쪽으로 이동해야 할때
            if x+1 < len(data) and data[y][x+1] == 1 and direction != 'left':
                x += 1
                direction = 'right'
            # 왼쪽으로 이동해야할때
            elif x-1 > -1 and data[y][x-1] == 1 and direction != 'right':
                x -= 1
                direction = 'left'
            # 좌우로 이동할 일이 없을때
            else:
                y += 1
                direction = ''
        # 시작점 하나에서 끝까지 갔을때, 도착점의 값이 2라면 시작점을 반환
        if data[y][x] == 2:
            return start
for t in range(1, 11):
    # 100 x 100 데이터 받아주고
    T = int(input())
    data = [list(map(int,input().split())) for i in range(100)]
    # 시작점은 1로 되어있을거니까 시작점 찾아주고
    start_idx = [i for i in range(len(data[0])) if data[0][i]]
    # 함수에 집어넣어서 끝값이 2인 시작점의 위치 반환해주고
    X = sadari(data, start_idx)
    print('#%d %d' %(T,X))
