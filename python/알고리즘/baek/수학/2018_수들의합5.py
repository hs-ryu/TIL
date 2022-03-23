
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