def solution(numbers):
    answer = [-1] * len(numbers)
    
    stack = []
    
    # [5,3,1,4,6,3]
    # [0,1,2,3,4,5]
    
    # stack : [0]
    # stack : [0,1]
    # stack : [0,1,2]
    # stack : [0,1,2]
    # -> i == 3 일때, numbers[-1] (= 2) 가 numbers[3] 보다 작다.
    # 따라서, answer[2] = numbers[3]이 된다.
    # 이후, numbers[-1] (=1) 가 numbers[3] 보다 작다.
    # 따라서, answer[1] = numbers[3]이 된다.
    # stack : [0,3]
    # 굳.
    
    for i in range(len(numbers)):
        while stack and numbers[stack[-1]] < numbers[i]:
            temp = stack.pop()
            answer[temp] = numbers[i]
        stack.append(i)
    return answer