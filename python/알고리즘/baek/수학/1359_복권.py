# 조합. n 최대가 8이므로 다 확인해도 됨.
def comb(level):
    if level >= n:
        if len(comb_data) == m:
            comb_set.append(comb_data[:])
        return
    comb_data.append(nums[level])
    comb(level+1)
    comb_data.pop(-1)
    comb(level+1)

n,m,k = map(int,input().split())
nums = [i for i in range(1,n+1)]
comb_set = []
comb_data = []
comb(0)
result = 0
a = [i for i in range(1,m+1)]

for c in comb_set:
    cnt = 0
    for i in range(m):
        if c[i] in a:
            cnt += 1
    if cnt >= k:
        result += 1    
print(result / len(comb_set))

