import heapq
from sys import stdin
# 힙이란? : 최댓값과 최소값을 찾는 연산을 빠르게 하기 위한 완전 이진 트리 형태.
# 최소 힙 : 부모 노드의 키 값이 자식 노드의 키 값보다 항상 작은 힙
# 최대 힙 : 부모 노드의 키 값이 자식 노드의 키 값보다 항상 큰 힙 

input = stdin.readline
n = int(input())
heap = []
for _ in range(n):
    x = int(input())
    if x == 0:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, x)