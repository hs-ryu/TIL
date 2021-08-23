n, q = map(int, input().split())
arr = []
for i in range(n):
    arr.append([i+1]+list(input().split()))
print(arr)
arr.sort(key=lambda x:(-int(x[2]) ,x[1], x[0]))
k = list(map(int,input().split()))
s = ''
for i in k:
    s += str(arr[i-1][0])
    s += ' '
print(s[:-1])