# 넣었다 뺐다?
# 최대 백만 * 알파니까 브루트포스

# pypy만 통과하는 코드
n,m = map(int,input().split())
contains_nums = list(map(int,input().split())) if m != 0 else [-1]
result = 0

max_num = 10 ** (n)
if contains_nums[0] != -1:
    for num in range(0,max_num):
        num = str(num).zfill(n)
        k = [str(i) for i in contains_nums]
        for i in range(len(num)):
            if num[i] in k:
                k.remove(num[i])
        if len(k) == 0:
            result += 1
else:
    result = max_num
print(result)



# 다르게 풀어보자.
# 필요한 숫자가 꼭 들어가는 부분만 생각해보자.

# n,m = map(int,input().split())
# contains_nums = list(map(int,input().split())) if m != 0 else [-1]
# result = 0