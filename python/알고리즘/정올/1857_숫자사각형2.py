n, m = map(int,input().split())

count = 0
for idx in range(1,n+1):
    for sub_idx in range(1, m+1):
        if idx % 2 == 0:
            count -= 1
            print(count, end=" ")
        else:
            count += 1
            print(count, end=' ')
    if idx % 2 == 1:
        count += m + 1
    else:
        count += m - 1
    print()