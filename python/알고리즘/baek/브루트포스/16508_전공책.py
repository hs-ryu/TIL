# 11%에서 틀림.

def search(level, arr):
    if level == n:
        global result
        visited = [0] * (len(t))
        total_price = 0
        for i in range(len(arr)):
            price, pos = arr[i]
            total_price += int(price)
            for k in range(len(t)):
                if t[k] in pos:
                    visited[k] = 1
        if sum(visited) == len(t):
            result = min(result,total_price)    
        return
    
    arr.append(books[level][:])
    search(level+1, arr)
    arr.pop(-1)
    search(level+1, arr)

t = input()
n = int(input())
books = [input().split() for _ in range(n)]
books.sort(key=lambda x:x[0])

for i in range(n):
    c,w = books[i]
    c = int(c)
    possible = set()
    for j in range(len(w)):
        if w[j] in t:
            possible.add(w[j])
    books[i][1] = possible

result = 100001 * 50
search(0,[])
if result == 100001 * 50:
    result = -1

print(result)