# 시발 시간초과 (실패실패)
from sys import stdin
input = stdin.readline

def search(arr, level):
    total = sum(arr)
    global standard
    # standard = 결과값과 k의 차이.
    if total > k + standard:
        return
    if level == 4:
        # print(arr, total, standard)
        temp_standard = abs(k-total)
        global result
        if temp_standard < standard:
            standard = temp_standard
            result = total
        elif temp_standard == standard:
            result = min(total,result)

    for i in range(level,4):
        for j in range(n):
            if check[i]:
                break
            # print(i, check[i])
            arr[i] = classes[i][j]
            check[i] = 1
            search(arr,level+1)
            arr[i] = 0
            check[i] = 0

t = int(input())
for _ in range(t):
    k,n = map(int,input().split())
    check = [0] * 4
    classes = []
    for i in range(4):
        classes.append(list(map(int,input().split())))
    standard = 40000001
    result = 40000001

    search([0,0,0,0],0)
    print(result)



