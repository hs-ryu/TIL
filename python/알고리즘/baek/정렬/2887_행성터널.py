# 옛날 코드 참조
# Kruskal
# 메모리 초과

def find_head(x):
    while head[x] != x:
        x = head[x]
    return x

N = int(input())
arr = []

for i in range(N):
    # m = list(map(int,input().split())) + [i]
    m = list(map(int,input().split()))
    arr.append(m)

connection = []

# # 여기서 메모리 많이 쓰나...?
for i in range(N-1):
    for j in range(i+1, N):
        connection.append([i, j, min(abs(arr[i][0]-arr[j][0]), abs(arr[i][1]-arr[j][1]), abs(arr[i][2]-arr[j][2]))])
#         # minV = 1000000001
#         # x_dis = abs(arr[i][0] - arr[j][0])
#         # y_dis = abs(arr[i][1] - arr[j][1])
#         # z_dis = abs(arr[i][2] - arr[j][2])
#         # if x_dis != 0 and x_dis < minV:
#         #     minV = x_dis
#         # if y_dis != 0 and y_dis < minV:
#         #     minV = y_dis
#         # if z_dis != 0 and z_dis < minV:
#         #     minV = z_dis
#         # connection.append([i, j, minV])


# for i in range(1, N):
#     connection.append([arr[i][-1], arr[i-1][-1], min(abs(arr[i][0]-arr[i-1][0]), abs(arr[i][1]-arr[i-1][1]), abs(arr[i][2]-arr[i-1][2]))])

# print(connection)



connection.sort(key=lambda x:x[2])
# print(connection)
head = list(range(N))
cnt = 0
i = 0
connection_length = len(connection)

result = 0

while cnt < N-1 and i < connection_length:
    temp = connection[i]
    if find_head(temp[0]) != find_head(temp[1]):
        result += temp[2]
        head[find_head(temp[0])] = find_head(temp[1])
        cnt += 1
    i += 1
# print(cnt)
print(result)


