# sawtooths = [list(input()) for _ in range(4)]
# print(sawtooths)
# k = int(input())

# for _ in range(k):
# 	idx, dir = map(int,input().split())
# 	idx -= 1
# 	# idx에 따라 회전시킬 놈 찾기.
# 	t1 = idx - 1
# 	t2 = idx + 1

# 	# 왼쪽놈들 체크
# 	while t1 >= 0:

# 		t1 -= 1
	

# 	# 오른쪽 놈들 체크
# 	while t2 < 4:

# 		t2 += 1
		
# 	# 돌려야 할 놈들 돌리기.

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

print(arr[0][0] * 1 + arr[1][0] * 2 + arr[2][0] * 4 + arr[3][0] * 8)