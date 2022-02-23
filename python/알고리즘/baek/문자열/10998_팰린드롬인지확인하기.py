s = list(input())
if len(s) % 2:
    a = s[:len(s)//2+1]
    b = list(reversed(s[len(s)//2:]))
    if a == b:
        print(1)
    else:
        print(0)
else:
    a = s[:len(s)//2]
    b = list(reversed(s[len(s)//2:]))
    if a == b:
        print(1)
    else:
        print(0)