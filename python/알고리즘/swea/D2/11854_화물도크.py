import sys
sys.stdin = open('5202_input.txt')

def selec_meeting(N,k,cnt):
    global max_meeting_cnt
    if cnt > max_meeting_cnt:
        max_meeting_cnt = cnt
    for i in range(k,N):
        if len(selec_list) == 0 or selec_list[-1][1] <= se_time[i][0]:
            selec_list.append(se_time[i])
            selec_meeting(N, k+1, cnt+1)
            selec_list.pop()
T = int(input())
for t in range(1, T+1):
    N = int(input())
    se_time = [list(map(int, input().split())) for _ in range(N)]
    se_time.sort(key=lambda x:x[1])
    selec_list = []
    max_meeting_cnt = 0
    selec_meeting(N, 0, 0)
    print('#%d %d' %(t, max_meeting_cnt))