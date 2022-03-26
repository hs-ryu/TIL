l = int(input().rstrip())

for _ in range(l):
    left = []
    right = []
    s = input().rstrip()

    for i in s:
        if i == '<':
            if left:
                right.append(left.pop())
        elif i == '>':
            if right:
                left.append(right.pop())
        elif i == '-':
            if left:
                left.pop()
        else:
            left.append(i)
    print(''.join(left)+''.join(reversed(right)))