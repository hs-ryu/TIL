
# 기름값 돌면서 최저값보다 더 작은값 나오면 갱신
n = int(input())
road = list(map(int, input().split()))
city = list(map(int, input().split()))

minv = city[0]
total = 0
for i in range(n-1):
    if minv > city[i]:
        minv = city[i]
    total += minv * road[i]
    
print(total)