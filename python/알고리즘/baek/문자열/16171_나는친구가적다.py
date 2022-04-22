st = list(input())
f = input()

nums = set(str(i) for i in range(0,10))

new_st = ""
for i in range(len(st)):
    if st[i] in nums:
        continue
    new_st += st[i]

if f in new_st:
    print(1)
else:
    print(0)