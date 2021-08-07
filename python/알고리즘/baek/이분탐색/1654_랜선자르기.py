k, n = map(int, input().split())
lan = [int(input()) for _ in range(k)]
left = 1
right = max(lan)

while (left <= right):
    mid = (left + right) // 2
    total = 0
    for i in lan:
        total += i // mid
    
    # 정답보다 잘게 잘랐다면 시작값을 방금값 + 1로
    if total >= n:
        left = mid + 1
    else:
        right = mid - 1

print(right)
