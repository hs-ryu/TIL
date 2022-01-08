n,k = map(int,input().split())

money = [100001] * (k+1)
money[0] = 0

dongjeon = []
for i in range(n):
    dongjeon.append(int(input()))

dongjeon.sort()


# dongjeon = 1 -> 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15
# dongjeon = 5 -> 0,0,0,0,0,1,2,3,4,5,2,3,4,5,6,3
# dongjeon = 12 -> 0,0,0,0,0,0,0,0,0,0,0,1,2,3,4

# money => 0,1,2,3,4,  1,2,3,4,5,2,3,  1,2,3,3


for i in range(n):
    for j in range(dongjeon[i],k+1):
        money[j] = min(money[j], money[j-dongjeon[i]] + 1)

if money[k] == 100001:
    money[k] = -1

print(money[k])

