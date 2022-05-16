n = int(input())
lopes = [int(input()) for _ in range(n)]
# print(lopes)
lopes.sort(reverse=True)


max_value = 0
k = 0
for i in range(len(lopes)):
    k += 1
    moolche = lopes[i] * k
    if moolche >= max_value:
        max_value = moolche

print(max_value)