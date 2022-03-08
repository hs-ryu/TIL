# l = int(input())
# s = list(map(int,input().split()))
# n = int(input())

# s.sort()

# idx = -1

# result = -1
# for i in range(l):
#     if n > s[i]:
#         idx = i
#     elif n == s[i]:
#         result = 0
#     else:
#         break

# if result == 0:
#     print(0)
# else:
#     # n이 원소들 보다 작은 경우
#     if idx < 0:
#         min_a = 1
#         max_b = s[0]
#         result = 0
        
#         for a in range(min_a,n+1):
#             for b in range(a+1,max_b):
#                 if b < n:
#                     break
#                 print(a,b)
#                 result += 1

#     else:
#         min_a = s[idx]+1
#         max_b = s[idx+1] if idx < l-1 else 1000
#         result = 0

#         s = set(s)

#         for a in range(min_a,n+1):
#             # print(a)
#             for b in range(a+1,max_b+1):
#                 if b < n:
#                     continue
#                 flag = 0 
#                 for k in range(a,b+1):
#                     if k in s:
#                         flag = 1
#                         break
#                 else:
#                     # print(a,b)
#                     result += 1
#                 if flag:
#                     break


#     print(result)









l = int(input())
s = list(map(int,input().split()))
n = int(input())

idx = -1
result = -1
s.sort()


# n의 위치 체크 (n이 집합의 가장 작은수 보다 작은지, 혹은 같은 수가 있는지)
for i in range(l):
    if n > s[i]:
        idx = i
    elif n == s[i]:
        idx = i
        result = 0
        break

# 같은 수가 있다면 구간에 포함할 수 있는게 없으므로, 개수는 0개
if result == 0:
    print(0)
# 같은 수가 없다면 2가지 경우가 있을것.
# 1. 집합내의 가장 작은수 보다 n이 작은 경우
# 2. 집합 내의 두 수 사이에 n이 있는 경우
else:
    result = 0
    # idx가 -1이면 집합 내의 가장 작은수 보다 n이 작은 경우임.
    if idx == -1:
        # 범위는 첫번째 수까지만 봐주면 됨.
        for i in range(1,s[0]-1):
            for j in range(i+1,s[0]):
                if n in set(range(i,j+1)):
                    print(i,j)
                    result += 1
    # 아니면 n이 집합 범위 내에 있는 경우임. 이때 위에서 찾은 idx를 활용해서 범위 설정해준다.
    else:
        for i in range(s[idx]+1,s[idx+1]-1):
            for j in range(i+1,s[idx+1]):
                if n in set(range(i,j+1)):
                    print(i,j)
                    result += 1
    print(result)
