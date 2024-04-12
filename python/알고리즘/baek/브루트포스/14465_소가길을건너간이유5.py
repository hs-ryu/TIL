N, K, B = map(int, input().split())

trafficlight = [1] * (N+1)

# 고장난 애들 체크
for _ in range(B):
    broken = int(input())
    trafficlight[broken] = 0

# 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0
# 5 번을 고치면 댐.

need = 0
for i in range(1, K+1):
    if trafficlight[i] == 0:
        need += 1

result = need

for i in range(2, N-K+2):
    # 2,3,4,5,6,7
    # ...
    # 5,6,7,8,9,10
    if trafficlight[i-1] == 0:
        need -= 1
    
    if trafficlight[i+K-1] == 0:
        need += 1
    
    result = min(result, need)

print(result)