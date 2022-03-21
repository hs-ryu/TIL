n,m = map(int,input().split())

if n == 0:
    print(0)
else:
    books = list(map(int,input().split()))

    box = 1
    x = m
    for i in range(n):
        if x >= books[i]:
            x -= books[i]
        else:
            box += 1
            x = m - books[i]
    print(box)