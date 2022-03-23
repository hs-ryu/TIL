
def search(x):
    hab = sum(x)
    if hab > n:
        return
    elif hab == n:
        global result
        result += 1
        return
    else:
        search(x + [x[-1]+1])

n = int(input())
result = 0
for i in range(1,n+1):
    search([i])
print(result)



n = int(input())
nums = [i for i in range(1,n+1)]

s,e = 0,0
result = 0

for temp in range(n):
    while e < n and s < n:
        s += nums[e]
        e += 1
    if s == n:
        result += 1
    s -= nums[temp]
print(result)