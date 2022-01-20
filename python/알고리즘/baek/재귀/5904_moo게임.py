
# S(0) = m o o
# S(1) = S(0) + m o o o + S(0) = m o o m o o o m o o
# S(2) = S(1) + m o o o o + S(1) = m o o m o o o m o o m o o o o m o o m o o o m o o

# def search(k,s):
#     # print(s,len(s),k)
#     if len(s) > n+1:
#         print(s[n-1])
#         return
#     m = "m" + "o" * (k+3)
#     search(k+1, s + m + s)

# n = int(input())
# k = 0
# s = "moo"
# search(k,s)



# m = s(k-1) + m + o*(k+2) + s(k-1)
# o = 나머지

def search(acc,cur,N):
    prev = (acc - cur) // 2
    if N <= prev:
        return search(prev, cur-1, N)
    elif N > prev + cur:
        return search(prev, cur-1, N-prev-cur)
    else:
        if N-prev-1:
            return "o"
        else:
            return "m"

N = int(input())
acc, n = 3, 0
while N > acc:
    n += 1
    acc = acc * 2 + n + 3
print(search(acc,n+3,N))


