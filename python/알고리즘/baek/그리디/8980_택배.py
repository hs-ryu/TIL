n, c = map(int, input().split())
m = int(input())
state = [0] * (n+1)

boxs = []
for i in range(m):
    boxs.append(list(map(int, input().split())))

boxs.sort(key=lambda x:(x[1], x[0]))
# print(boxs)
send = 0
for i in range(m):
    s = boxs[i][0]
    e = boxs[i][1]
    box_cnt = boxs[i][2]

    maxV = 0
    for idx in range(s, e+1):
        maxV = max(maxV, state[idx])
    
    possible_box_cnt = min(c - maxV, box_cnt)
    send += possible_box_cnt

    for idx in range(s, e):
        state[idx] += possible_box_cnt
print(send)