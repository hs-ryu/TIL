# front = -1
# rear = -1
# N = 4
# def enQueue(q, data):
#     global rear
#     if rear >= len(q) - 1:
#         print('overflow')
#     else:
#         rear += 1
#         q[rear] = data
#
# def deQueue(q):
#     global front
#     global rear
#     if front == rear:
#         print('underflow')
#     else:
#         front += 1
#         x = q[front]
#         return x
#
# q = [0] * N
# enQueue(q, 1)
# enQueue(q, 2)
# enQueue(q, 3)
# enQueue(q, 4)
# enQueue(q, 5)
# x1 = deQueue(q)
# x2 = deQueue(q)
# x3 = deQueue(q)
# print(q, x1, x2, x3)


'''문제
큐를 구현하여 다음 동작을 확인해 봅시다.
세 개의 데이터 1, 2, 3을 차례로 큐에 삽입하고
큐에서 세 개의 데이터를 차례로 꺼내서 출력한다.
1, 2, 3이 출력 되야 함
'''

def enQueue(q, data):
    global rear
    if rear >= len(q) - 1:
        print('overflow')
    else:
        rear += 1
        q[rear] = data

def deQueue(q):
    global front
    global rear
    if front == rear:
        print('underflow')
    else:
        front += 1
        x = q[front]
        return x

T = int(input())
front = -1
rear = -1
N = 4
q = [0] * N
for t in range(1, T+1):
    answer = []
    enQueue(q, 1)
    enQueue(q, 2)
    enQueue(q, 3)
    answer.append(deQueue(q))
    answer.append(deQueue(q))
    answer.append(deQueue(q))
    ans = ' '.join(list(map(str,answer)))
    print('#%d %s' % (t, ans))