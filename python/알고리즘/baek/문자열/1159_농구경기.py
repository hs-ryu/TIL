n = int(input())

nameset = dict()

for _ in range(n):
    name = input()
    if name[0] in nameset:
        nameset[name[0]] += 1
    else:
        nameset[name[0]] = 1

result = []
for k in nameset.keys():
    if nameset[k] >= 5:
        result.append(k)
if result:
    result.sort()
    print(''.join(result))
else:
    print('PREDAJA')