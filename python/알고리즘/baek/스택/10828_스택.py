from sys import stdin
input = stdin.readline

n = int(input())

s = []
for _ in range(n):
    x = list(input().split())
    if x[0] == "push":
        s.append(x[1])
    elif x[0] == "pop":
        if len(s):
            k = s.pop(-1)
            print(k)
        else:
            print(-1)
    elif x[0] == "size":
        print(len(s))
    elif x[0] == "empty":
        print(0 if len(s) else 1)
    else:
        print(s[-1] if len(s) else -1)
    