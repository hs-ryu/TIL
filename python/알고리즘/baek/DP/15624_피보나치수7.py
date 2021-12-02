# 메모리 초과
# n = int(input())
# k = [0] * 1000001
# k[0] = 0
# k[1] = 1
# k[2] = 1
# for i in range(3, n+1):
#     k[i] = k[i-1] + k[i-2]
# print(k[n] % 1000000007)

n = int(input())
k = [0] * 1000001
k[0] = 0
k[1] = 1
k[2] = 1
for i in range(3, n+1):
    k[i] = (k[i-1] + k[i-2]) % 1000000007
print(k[n])