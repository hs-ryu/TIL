# 중복 커버되어 있는 것에 대한 대책.
import sys
sys.stdin = open('test_case.txt')

from pprint import pprint

def answer(place):
    for i in range(len(place)):
        for j in range(len(place[0])):
            if place[i][j] != 'X' and place[i][j] != 'H':
                x = ord(place[i][j])
                y = ord('A')
                for k in range(1, ord(place[i][j]) - ord('A') + 2):
                    # 상
                    if place[i - k][j] == 'H':
                        place[i - k][j] = 'X'
                    # 하
                    if place[i + k][j] == 'H':
                        place[i + k][j] = 'X'
                    # 우
                    if place[i][j + k] == 'H':
                        place[i][j + k] = 'X'
                    # 좌
                    if place[i][j - k] == 'H':
                        place[i][j - k] = 'X'
    return place

T = int(input())
for t in range(1, T+1):
    N = int(input())
    place = [list('XXX' + input() + 'XXX') for _ in range(N+1)]
    padding = [list('X' * (N + 6)) for i in range(3)]
    place.extend(padding)
    place = padding + place
    pprint(place)
    print('-----------------')
    result = answer(place)
    cnt = 0
    for i in range(3, len(result) - 3):
        for j in range(3, len(result[0])- 3):
            if result[i][j] == 'H':
                cnt += 1
    print(cnt)