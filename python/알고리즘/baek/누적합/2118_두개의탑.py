n = int(input())
arr = [0] * (n+1)
# 반시계 거리 + 시계 거리 = 전체 거리
# 시계 거리가 반시계 거리보다 크면 더 안봐도 될듯
total = 0
for i in range(n):
    arr[i] = int(input())
    total += arr[i]
# print(arr)
# print(total)
# 변수 2개?
s = 0
e = 0

# 현재 시계방향 거리값
x = arr[0]
answer = 0
while (s <= e and e < n):
    # 더 작은값 선택
    minv = min(x, total - x)
    # print("minv", minv)

    # 현재 시계방향 거리값이 갱신된 minv랑 같다? 아직 시계방향이 더 짧은거.
    if (x == minv):
        e += 1
        x += arr[e]
    # 아니면, 반시계 방향으로 가는게 더 짧은거니까 다음거 찾자.
    else:
        x -= arr[s]
        s += 1
    # 정답 갱신
    answer = max(answer, minv)
    
print(answer)