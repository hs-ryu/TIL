N, d, k, c = map(int, input().split())

rail = [int(input()) for _ in range(N)]

selected = [0] * 3001

# 현재 선택한 초밥의 종류
kinds = 0

# 초밥의 종류를 최대한 많이 선택한 경우
maximum_kinds = 0

for i in range(0,k):
    if selected[rail[i]] == 0:
        kinds += 1
    selected[rail[i]] += 1

maximum_kinds = kinds + 1 if selected[c] == 0 else kinds

for i in range(N):
    # 앞쪽꺼 하나 제외, 뒤쪽꺼 하나 더하고
    front = i
    end = i + k
    
    if end >= N:
        end -= N
    
    selected[rail[front]] -= 1
    
    if selected[rail[front]] == 0:
        kinds -= 1
    
    if selected[rail[end]] == 0:
        kinds += 1
    selected[rail[end]] += 1
    
    if selected[c] == 0:
        maximum_kinds = max(maximum_kinds, kinds + 1)
    else:
        maximum_kinds = max(maximum_kinds, kinds)

print(maximum_kinds)