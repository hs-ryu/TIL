t = int(input())

for _ in range(t):
    one, two = input().split()
    one = int(one,2)
    two = int(two,2)
    result = one + two
    result = str(bin(result))[2:]
    print(result)