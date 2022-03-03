l = int(input())
s = list(map(int,input().split()))
n = int(input())

s.sort()

idx = -1

result = -1
for i in range(l):
    if n > s[i]:
        idx = i
    elif n == s[i]:
        result = 0
    else:
        break

if result == 0:
    print(0)
else:
    # n이 원소들 보다 작은 경우
    if idx < 0:
        min_a = 1
        max_b = s[0]
        result = 0
        
        for a in range(min_a,n+1):
            for b in range(a+1,max_b):
                if b < n:
                    break
                print(a,b)
                result += 1

    else:
        min_a = s[idx]+1
        max_b = s[idx+1] if idx < l-1 else 1000
        result = 0

        s = set(s)

        for a in range(min_a,n+1):
            # print(a)
            for b in range(a+1,max_b+1):
                if b < n:
                    continue
                flag = 0 
                for k in range(a,b+1):
                    if k in s:
                        flag = 1
                        break
                else:
                    # print(a,b)
                    result += 1
                if flag:
                    break


    print(result)