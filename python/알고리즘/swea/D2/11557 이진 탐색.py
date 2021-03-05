import sys
sys.stdin = open('sample_input.txt')

def search(PA, left, right):
    center = 0
    cnt = 0
    while center != PA:
        center = (left + right) // 2
        cnt += 1
        if center == PA:
            break
        elif center < PA:
            left = center
        elif center > PA:
            right = center
    return cnt
T = int(input())
for t in range(1, T+1):
    P, PA, PB = map(int, input().split())
    left = 1
    right = P
    A = search(PA, left, right)
    B = search(PB, left, right)
    result = '0'
    if A < B:
        result = 'A'
    elif A > B:
        result = 'B'
    # 한줄로 쓰면 ???  result = 'A' if A<B else '0' if A = B else 'B'

    print('#%d %s' % (t, result))

