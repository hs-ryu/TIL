M,N,L = map(int, input().split())

sadae = list(map(int, input().split()))

animals = [list(map(int, input().split())) for _ in range(N)]

sadae.sort()
result = 0

for i in range(N):
    x,y = animals[i]

    if y > L:
        continue
    
    # l = abs(s - x) + y
    # x - s + y
    # s - x + y
    # l = x - s + y -> s = x + y - l -> 최소 (7 + 2 - 4 = 5)
    # l = s - x + y -> s = x - y + l -> 최대 (7 - 2 + 4 = 9)
    
    minX = x + y - L
    maxX = x - y + L
    # print("x,y : ", x,y, L)
    # print("range : ", minX, maxX)

    l = 0
    r = M - 1
    while l <= r:
        middle = (l + r) // 2
        if minX <= sadae[middle] and  sadae[middle] <= maxX:
            result += 1
            break
        elif sadae[middle] < minX:
            l = middle + 1
        elif sadae[middle] > maxX:
            r = middle - 1

print(result)

    
