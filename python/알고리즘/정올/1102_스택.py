n = int(input())
stack = []
for i in range(n):
    s = input()
    if len(s) > 1:
        act, num = s.split()
        stack.append(int(num))
    else:
        if s == 'o':
            try:
                out = stack.pop(-1)
            except:
                out = 'empty'
            print(out)
        elif s == 'c':
            print(len(stack))
