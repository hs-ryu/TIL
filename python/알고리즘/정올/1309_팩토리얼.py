def factorial(i):
    if i == 1:
        print('1! = 1')
        return 1
    print(f'{i}! = {i} * {i-1}!')
    return i * factorial(i-1)
    
n = int(input())
print(factorial(n))