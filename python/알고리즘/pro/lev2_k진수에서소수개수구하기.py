def solution(n, k):
    
    def isPrime(x):
        cnt = 0
        for i in range(1,int(x**(0.5))+1):
            if x % i == 0:
                cnt += 1
            if cnt > 1:
                return False
        return True
    
    answer = 0
    changed_num = ""
    while n:
        x = n % k
        n = n // k
        changed_num += str(x)
    num = ''
    for i in range(len(changed_num)-1,-1,-1):
        num += changed_num[i]
    
    arr = num.split('0')
    print(arr)
    for i in range(len(arr)):
        if arr[i] and arr[i] != '1':
            if isPrime(int(arr[i])):
                answer += 1
    return answer