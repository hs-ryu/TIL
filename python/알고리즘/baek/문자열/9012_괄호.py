t = int(input())

for _ in range(t):
    st = input()

    stack = []
    check = True
    for i in range(len(st)):
        if st[i] == "(":
            stack.append(st[i])
        else:
            if stack:
                stack.pop(-1)
            else:
                check = False
                break
    if stack:
        check = False
    if check == False:
        print("NO")
    else:
        print("YES")
