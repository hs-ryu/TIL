n = int(input())
steels = list(map(int,input().split()))

# 4개면, 3번 잘라야함 무조건.
# 3,5,4,2 라면, 5,4,3,2 로 정렬해서, 5 * 9로 한번, 4 * 5로 한번, 3 * 2로 한번 자르는게 최소임. 45 + 20 + 6 -> 71
# 12 * 2로 한번, 9 * 3으로 한번, 5 * 4로 한번 자르면 -> 24 + 27 + 20 -> 71 ? 뭐지

# 4,5,6,7이면, 7 * 15 + 9 * 6 + 4 * 5 = 105 + 54 + 20 = 179
# 4 * 18 + 13 * 5 + 6 * 7 = 72 + 65 + 42 = 137 + 42 = 179? 왜 똑같지

# 4,5,6 => 11 * 4 + 5 * 6 = 44 + 30 = 74
# 9 * 6 + 4 * 5 = 54 + 20 = 74 똑같네 

steels.sort(reverse=True)
hab = sum(steels)

result = 0
for i in range(n):
    hab -= steels[i]
    result += hab * steels[i]
print(result)

