result = []
while True:
    n = input()
    if n == '0':
        break
    int_n = list(map(int, n))
    n = list(n)
    reverse_num = reversed(n)
    sum_num = sum(int_n)
    result.append([int(''.join(reverse_num)), sum_num])

for i in range(len(result)):
    print(*result[i])