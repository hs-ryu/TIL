def rotate(i, dir):
    #시계방향
    if dir == 1 :
        arr[i].insert(0,arr[i].pop())
    #반시계방향
    elif dir == -1:
        arr[i].append(arr[i].pop(0))

arr = []
for _ in range(4):
    arr.append(list(input()))
K = int(input())

for _ in range(K):
    i, dir = map(int,input().split())
    rotate_arr = [[i-1,dir]]

    #오른쪽
    x = i-1
    tempdir = dir
    while x + 1 <= 3:
        if arr[x][2] != arr[x+1][6] :
            tempdir = -tempdir
            rotate_arr.append([x+1, tempdir])
        elif arr[x][2] == arr[x+1][6]:
            break
        x += 1

    #왼
    x = i-1
    tempdir = dir
    while x - 1 >= 0 :
        if arr[x][6] != arr[x-1][2]:
            tempdir = -tempdir
            rotate_arr.append([x -1, tempdir])
        elif arr[x][6] == arr[x-1][2]:
            break
        x -= 1
    for x, dd in rotate_arr:
        rotate(x,dd)

answer = [list(map(int, arr[i])) for i in range(len(arr))]
# print(arr)
result = 0
for i in range(4):
    result += answer[i][0] * (2 ** i)

print(result)