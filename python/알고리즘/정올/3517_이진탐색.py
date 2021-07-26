n = int(input())
a = list(map(int, input().split()))
q = int(input())
b = list(map(int, input().split()))


answer = []
for num in b:
    left = 0
    right = len(a) - 1
    while left <= right:
        middle = (left+right) // 2
        if a[middle] == num:
            answer.append(middle)
            break
        if a[middle] > num:
            right = middle-1
        else:
            left = middle + 1
    else:
        answer.append(-1)

print(*answer)