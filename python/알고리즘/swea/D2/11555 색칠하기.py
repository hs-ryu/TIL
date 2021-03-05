import sys
sys.stdin = open('sample_input_color.txt')


T = int(input())
for t in range(1,T+1):
    grid = [[0 for _ in range(10)] for _ in range(10)]
    N = int(input())
    k = []
    cnt = 0
    for i in range(N):
        k.append(list(map(int,input().split())))
    for i in k:
        for j in range(i[0], i[2]+1):
            for m in range(i[1], i[3]+1):
                if grid[j][m] != i[4]:
                    grid[j][m] += i[4]
                if grid[j][m] == 3:
                    cnt += 1
    print('#%d %d' %(t,cnt))

# 델타함수를 써서도 한번 풀어보자.



