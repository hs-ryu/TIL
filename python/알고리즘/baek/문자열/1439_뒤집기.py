s = input()

s_0 = s.split("1")
s_1 = s.split("0")


# print(s_0)
# print(s_1)

result1 = 0
for i in range(len(s_0)):
    if s_0[i]:
        result1 += 1

result2 = 0
for i in range(len(s_1)):
    if s_1[i]:
        result2 += 1

result = min(result1, result2)
print(result)