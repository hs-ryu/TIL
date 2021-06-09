start, end = map(int, input().split())
if start > end:
    for i in range(start, end-1, -1):
        for j in range(1,9,3):
            print("%d * %d =%3d   %d * %d =%3d   %d * %d =%3d" %(i, j, i*j, i, j+1, i*(j+1), i, j+2, i*(j+2)))
        print()
else:
    for i in range(start, end+1):
        for j in range(1,9,3):
            print("%d * %d =%3d   %d * %d =%3d   %d * %d =%3d" %(i, j, i*j, i, j+1, i*(j+1), i, j+2, i*(j+2)))
        print()