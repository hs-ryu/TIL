n,k = map(int,input().split())

characters = []
for i in range(n):
    characters.append(int(input()))

# 이분탐색해야하니까.
characters.sort()

l = 0
r = 987654321

result = 0
while l <= r:
    middle = (l + r) // 2
    
    total = 0
    for i in range(n):
        if middle > characters[i]:
            total += middle - characters[i]
    
    if total <= k:
        l = middle + 1
        result = max(middle,result)
    else:
        r = middle - 1

print(result)
