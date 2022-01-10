n = int(input())

satisfy = [0] * (n+1)
snack = [0] * (n+1)
for i in range(1,n+1):
    snack[i] = int(input())

satisfy[1] = snack[1]
result = satisfy[1]

for i in range(2,n+1):
    satisfy[i] = snack[i]
    for j in range(1,i):
        if snack[j] < snack[i]:
            satisfy[i] = max(satisfy[i], satisfy[j] + snack[i])
    result = max(result, satisfy[i])
print(result)
