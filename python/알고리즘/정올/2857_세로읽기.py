string = list(input() for _ in range(5))
new_string = ''
k = 0
for i in range(5):
    if k < len(string[i]):
        k = len(string[i])
for i in range(k):
    for j in range(5):
        try:
            new_string += string[j][i]
        except:
            continue
print(new_string)
