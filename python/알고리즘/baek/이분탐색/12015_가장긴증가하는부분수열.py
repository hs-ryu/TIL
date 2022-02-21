
# # 이중 반복문 -> 시간초과. 11568번은 통과함.
# n = int(input())
# a = list(map(int,input().split()))
# dp = [1] * n
# # 배열 a 탐색
# for i in range(1,n):
#     # 0 ~ i-1 까지 현재(i번째)까지 작은수가 있는지 없는지 확인.
#     for j in range(i):
#         # 현재 수가 이전 수보다 크다면. 길이 체크.
#         if a[j] < a[i]:
#             if dp[i] > dp[j]+1:
#                 continue
#             else:
#                 dp[i] = dp[j]+1
# print(max(dp))


# 이분탐색 풀이 (nlogn)
n = int(input())
a = list(map(int,input().split()))

result = [0]
for i in range(n):
    x = a[i]
    if x > result[-1]:
        result.append(x)
    else:
        l = 0
        r = len(result)-1
        while l < r:
            m = (l + r)//2
            if result[m] >= x:
                r = m
            else:
                l = m+1
        result[r] = x
print(len(result)-1)
