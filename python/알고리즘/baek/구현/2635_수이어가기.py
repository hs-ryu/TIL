from copy import deepcopy
n = int(input())

max_cnt = 0
max_list = []

for i in range(1,n+1):
    now_list = [n,i]
    j = 2
    cnt = 2
    while True:
        temp = now_list[j-2] - now_list[j-1]
        if temp < 0:
            break
        now_list.append(temp)
        j += 1
        cnt += 1
    if cnt > max_cnt:
        max_cnt = cnt
        max_list = deepcopy(now_list)
print(max_cnt)
print(*max_list)



    
