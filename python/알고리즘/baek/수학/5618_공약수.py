n = int(input())

def find_yarksoo(a,b):
    if (a == 0):
        return b
    return find_yarksoo(b % a, a)


if n == 2:
    a,b = map(int,input().split())
    yarksoo = find_yarksoo(a,b)
    for i in range(1, yarksoo//2 + 1):
        if not yarksoo % i:
            print(i)
    print(yarksoo)

else:
    a,b,c = map(int,input().split())
    yarksoo = find_yarksoo(a,find_yarksoo(b,c))
    for i in range(1, yarksoo // 2 + 1):
        if not yarksoo % i:
            print(i)
    print(yarksoo)