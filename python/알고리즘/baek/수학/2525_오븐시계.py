a,b = map(int,input().split())
t = int(input())

k = b + t

while k >= 60:
    a += 1
    k -= 60

if a >= 24:
    a -= 24

print(a, k)