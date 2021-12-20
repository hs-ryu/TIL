from sys import stdin
input = stdin.readline

n = int(input())
nums = list(map(int,input().split()))

# # subtask 1
# if n == 3:
#     # 단조증가 수열
#     if nums[0] <= nums[1] <= nums[2]:
#         print(2)
#     # 단조감소 수열
#     elif nums[0] >= nums[1] >= nums[2]:
#         print(2)
#     else:
#         print(3)

# # subtask 2~3
# else:

#     k = 2
#     max_k = 2
#     for i in range(n-2):
#         if nums[i] <= nums[i+1] <= nums[i+2]:
#             if max_k < k:
#                 max_k = k
#             k = 2
#         elif nums[i] >= nums[i+1] >= nums[i+2]:
#             if max_k < k:
#                 max_k = k
#             k = 2
#         else:
#             k += 1
#     if max_k < k:
#         max_k = k
#     print(max_k)


from sys import stdin
input = stdin.readline

n = int(input())
nums = list(map(int,input().split()))

# 단조 증가, 단조 감소 수열이 아니면 길이 + 1
# 단조 증가, 단조 감소 수열이면 길이 비교 하고 변경 후 2로 초기화
k = 2
max_k = 2
for i in range(n-2):
    if nums[i] <= nums[i+1] <= nums[i+2]:
        if max_k < k:
            max_k = k
        k = 2
    elif nums[i] >= nums[i+1] >= nums[i+2]:
        if max_k < k:
            max_k = k
        k = 2
    else:
        k += 1
if max_k < k:
    max_k = k
print(max_k)