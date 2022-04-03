from sys import stdin
input = stdin.readline


def something(jump, val):
    i = 0
    while i < n:
        a[i] = a[i] + val
        i = i + jump
        

n,k = map(int,input().split())
x = list(map(int,input().split()))
a = [0] * n
# x의 중복된 개수를 구해준다.

x_dic = dict()

for i in range(len(x)):
    if x[i] in x_dic:
        x_dic[x[i]] += 1
    else:
        x_dic[x[i]] = 1

for jump,val in x_dic.items():
    something(jump,val)

# 누적합 계산

hab = [0] * n
hab[0] = a[0]
for i in range(1, n):
    hab[i] = hab[i-1] + a[i]
# print(hab)

q = int(input())
for _ in range(q):
    l,r = map(int,input().split())
    if l != 0:
        print(hab[r]-hab[l-1])
    else:
        print(hab[r])
    