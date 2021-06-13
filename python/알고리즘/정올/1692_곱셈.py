x = input()
y = input()
total_result = 0
k = 0
for i in range(len(y)-1,-1,-1):
    line_result = int(y[i]) * int(x)
    print(line_result)
    total_result += line_result * (10 ** k)
    k += 1
print(total_result)