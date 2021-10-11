# 1,2,3,4,5,6,7
# 4,5,6,7,1,2
# 2, 5, 8

n, k = map(int, input().split())

people = [i for i in range(1,n+1)]

cnt = 1
i = -1
answer =[]
while cnt < n:
    i += k
    if i > n-1:
        i = i-n
    answer.append(people[i])
    

    cnt += 1
