import sys
sys.stdin = open('input.txt')

for t in range(1,11):
    dump = int(input())
    box = list(map(int, input().split()))
    i = 0
    while i < dump:
        max_value, min_value = box[0], box[0]
        max_idx, min_idx = 0, 0
        for idx, value in enumerate(box):
            if value > max_value:
                max_value = value
                max_idx = idx
            if value < min_value:
                min_value = value
                min_idx = idx
        box[max_idx] -= 1
        box[min_idx] += 1
        i += 1
    max_value, min_value = box[0], box[0]
    for i in range(len(box)):
        if box[i] > max_value:
            max_value = box[i]
        if box[i] < min_value:
            min_value = box[i]
    print('#%d %d' %(t, max_value-min_value))


# 무의미한 경우가 있다(평탄화가 완료된 경우). 이때는 dump가 0이 아니더라도 계속 돌려봤자 의미가 없다.
'''
최대값 - 최소값 = 1인 경우에는 그만 돌리자라는 if문 작성해주면 실행 시간 많이 줄일 수 있을듯!
내가 한 방법 외에도, 각 높이 정보가 들어간 카운트 리스트를 작성하여 정렬 가능하다.
'''