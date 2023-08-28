n = int(input())

merchans = [int(input()) for _ in range(n)]

merchans.sort(reverse=True)

result = 0

for i in range(n):
    if(i%3!=2):
        result += merchans[i]
print(result)