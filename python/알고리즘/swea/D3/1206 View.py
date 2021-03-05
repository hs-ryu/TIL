import sys
sys.stdin = open('input.txt')

for T in range(1, 11):
    t = int(input())
    n = list(map(int, input().split()))
    answer = 0
    for i in range(2, t-2):
        ans_list = [n[i-2], n[i-1], n[i+1], n[i+2]]
        maxV = 0
        for j in ans_list:
            if j > maxV:
                maxV = j
        if n[i] > maxV:
            answer += n[i] - maxV
    print("#%d %d" % (T, answer))