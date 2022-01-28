n = int(input())

tropies = []
for i in range(n):
    tropies.append(int(input()))

left = 0
right = 0

temp = 0
for i in range(n):
    if tropies[i] > temp:
        left += 1
        temp = tropies[i]
temp = 0
for i in range(n-1,-1,-1):
    if tropies[i] > temp:
        right += 1
        temp = tropies[i]
print(left)
print(right)