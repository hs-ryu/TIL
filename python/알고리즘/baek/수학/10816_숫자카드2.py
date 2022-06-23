from sys import stdin
input = stdin.readline

n = int(input())
numbers = list(map(int,input().split()))

m = int(input())
finds = list(map(int,input().split()))

re_dict = dict()
for i in range(n):
    if numbers[i] in re_dict:
        re_dict[numbers[i]] += 1
    else:
        re_dict[numbers[i]] = 1

result = [0] * m
for i in range(m):
    if finds[i] in re_dict:
        result[i] = re_dict[finds[i]]
print(*result)