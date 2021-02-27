stack = []

# value를 스택의 맨 뒤에 추가한다.
def push(value):
    stack.append(value)
def pop():
    if len(stack) == 0:
        print('stack underflow')
        return
    return stack.pop()

N = 3
stack2 = [''] * N
top = -1

def push2(value):
    global top
    if top >= len(stack2) - 1:
        print('overflow')
        return
    top += 1
    stack2[top] = value

def pop2():
    global top
    if top < 0:
        print('underflow')
        return
    x = stack2[top]
    stack2[top] = ''
    top -= 1
    return x


# push(1)
# push(2)
# push(3)
# print(stack)
# pop()
# pop()
# push(4)
# push(5)
# pop()
# print(stack)

print(stack2)
push2(1)
push2(2)
push2(3)
push2(4)
print(stack2)
pop2()
pop2()
print(stack2)
push2(4)
push2(5)
pop2()
pop2()
pop2()
pop2()
print(stack2)

###################################
def fibo1(n):
    # len(memo) <= n에 위배되면, 이미 값이 구해져 있다는 뜻임.
    # n >= 2 는 0,1은 구하지 않겠단느 뜻.(이미 memo는 [0,1]로 초기화 되어 있으므로)
    if n >= 2 and len(memo) <= n:
        memo.append(fibo1(n-1) + fibo1(n-2))
    return memo[n]
memo = [0,1]

print(fibo1(10))
print(memo)
###################################

# 이 방법은 조금더 직관적이고 이해하기 쉽지만, memo2의 길이가 정해져 있기 때문에 설정된 값 이상의 경우 overflow가 발생할수 있고,
# 값이 없는 부분도 -1로써 표현된다.
memo2 = [-1] * 21
memo2[0] = 0
memo2[1] = 1

def fibo2(n):
    if memo2[n] == -1:
        memo2[n] = fibo2(n-1) + fibo2(n-2)
    return memo2[n]

print(fibo2(10))
print(memo2)

###################################
def func_A(level):
    if level >= 3:
        return
    print('func_A1',level)
    func_A(level+1)
    print('func_A2',level)

func_A(0)
###################################

def func_B(level):
    if level >= 3:
        return
    print('func_B1', level)
    func_B(level+1)
    print('func_B2', level)
    func_B(level+1)
    print('func_B3', level)

func_B(0)

########################
V, E = 7, 8
edges = [(1, 2), (1, 4), (1, 5), (2, 3), (3, 4), (3, 7), (4, 6), (5, 6)]
AL = [[] for _ in range(V+1)]
print(AL)
# 구현해 보세요
for s, e in edges:
    AL[s].append(e)
    AL[e].append(s)
for v in range(1, V+1):
    if AL[v]:
        print(v, AL[v])

