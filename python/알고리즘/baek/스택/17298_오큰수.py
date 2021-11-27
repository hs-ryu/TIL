n = int(input())
a = list(map(int, input().split()))
k = [-1] * n
stack = [0]

i = 1
while stack and i < n:
    print(stack)
    while stack and a[stack[-1]] < a[i]:
        k[stack[-1]] = a[i]
        stack.pop()
    stack.append(i)
    i += 1

print(*k)