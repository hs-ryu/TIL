n = input()

length = len(n)
half = length//2

c1 = 0
for i in range(half):
    c1 += int(n[i])
c2 = 0
for i in range(half,len(n)):
    c2 += int(n[i])

if c1 == c2:
    print("LUCKY")
else:
    print("READY")