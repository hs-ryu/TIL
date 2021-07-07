n = int(input())
queue = []
result = []
for i in range(n):
    s = input()
    if len(s) > 1:
        act, num = s.split()
        queue.append(int(num))
    else:
        if s == 'o':
            try:
                out = queue.pop(0)
            except:
                out = 'empty'
            print(out)
        elif s == 'c':
            print(len(queue))
