from sys import stdin
input = stdin.readline

n,m = map(int,input().split())
string_set = set()
for i in range(n):
    string_set.add(input())

result = 0
for i in range(m):
    temp = input()
    if temp in string_set:
        result += 1
print(result)
