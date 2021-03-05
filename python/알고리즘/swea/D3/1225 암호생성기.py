import sys
sys.stdin = open('input.txt')


def password(data):
    # 첫번째거 pop
    # pop한 값에서 1,2,3,4,5 순으로 빼줌 한 싸이클

    # 만약 빼준 값이 0보다 작다? 0으로 만들고 맨 뒤에 append 해주고 종료
    # 맨 뒤로 보내줌
    while True:
        i = 1
        while i < 6:
            x = data.pop(0)
            x -= i
            if x <= 0:
                x = 0
                data.append(x)
                return data
            data.append(x)
            i += 1

for t in range(1, 11):
    T = int(input())
    data = list(map(int, input().split()))
    result = password(data)
    res = ' '.join(list(map(str, result)))
    print('#%d %s' %(T, res))


