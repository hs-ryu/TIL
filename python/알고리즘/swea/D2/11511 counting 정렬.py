import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T+1):
    N = int(input())
    D = input().split()
    maxV = 0
    for i in range(len(D)):
        if int(D[i][0]) > maxV:
            maxV = int(D[i][0])
    count_list = [0] * (maxV+1)
    result = [0] * len(D)
    for i in range(len(D)):
        count_list[int(D[i][0])] += 1
    for i in range(len(count_list)-1):
        count_list[i+1] += count_list[i]
    for i in range(len(result)-1, -1, -1):
        count_list[int(D[i][0])] -= 1
        result[count_list[int(D[i][0])]] = D[i]
    dab = ' '.join(result)
    print('#%d %s' %(t, dab))


