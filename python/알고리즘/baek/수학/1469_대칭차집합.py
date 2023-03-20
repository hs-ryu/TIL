import sys
input = sys.stdin.readline
A,B = map(int,input().rstrip().split())
a = set(list(map(int,input().rstrip().split())))
b = set(list(map(int,input().rstrip().split())))
result = len(a)+len(b) - 2 * (len(a) - len(a-b))

print(result)