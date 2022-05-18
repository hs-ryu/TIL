
# 입력이 작아, 비효율적인 방식으로 풀었음.

"""

# 최대 공약수구하는 재귀함수.
def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a % b)

# 두 수의 최소 공배수 = (a * b) / (두 수의 최대공약수)
"""


def solution(arr):
    def LCM(a,b):
        a_list = set()
        for i in range(1, b+1):
            a_list.add(a * i)
        for i in range(1, a+1):
            value = i * b
            if value in a_list:
                return value
    answer = 0
    
    if len(arr) == 1:
        return arr[0]
    while len(arr) > 1:
        a = arr.pop(-1)
        b = arr.pop(-1)
        k = LCM(a,b)
        arr.append(k)
    answer = arr[0]
        
    return answer