n,k = map(int,input().split())
kids = list(map(int,input().split()))

# 1,3,5,6,10
# -> 연결되어있는 애들끼리 묶어야하니까 인접한 애들끼리 키차이 구해서?
# 2, 2, 1, 4 -> 이 중에서 큰거 k만큼 제외? -> 정렬해서 n-k-1까지만 더해주기
# 무러 골드 5.. 이게?

subtitude = [0] * (n-1)
for i in range(1,n):
    subtitude[i-1] = kids[i] - kids[i-1]
subtitude.sort()

print(sum(subtitude[:n-k]))