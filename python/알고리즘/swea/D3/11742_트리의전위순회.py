'''
첫 줄에는 트리의 정점의 총 수 V가 주어진다. 그 다음 줄에는 V-1개 간선이 나열된다.
간선은 그것을 이루는 두 정점으로 표기된다. 간선은 항상 “부모 자식” 순서로 표기된다.
아래 예에서 두 번째 줄 처음 1과 2는 정점 1과 2를 잇는 간선을 의미하며 1이 부모, 2가 자식을 의미한다.
간선은 부모 정점 번호가 작은 것부터 나열되고, 부모 정점이 동일하다면 자식 정점 번호가 작은 것부터 나열된다.

다음 이진 트리 표현에 대하여 전위 순회하여 정점의 번호를 출력하시오.
13 ← 정점의 개수
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13


'''


import sys
sys.stdin = open('input_tree01.txt')

def jeonwi(t):
    if t:
        result.append(t)
        jeonwi(tree[t][0])
        jeonwi(tree[t][1])


N = int(input())
gansun = list(map(int, input().split()))
tree = [[] for _ in range(N)]
tree.append([])
result = []
for i in range(0, len(gansun), 2):
    tree[gansun[i]].append(gansun[i+1])

# 그냥 최초에 0으로 초기화 해놓고
'''
if ch1[p] == 0:
    ch1[p] == c
else
    ch2[p] == c
'''
# 방식으로 해도 됨.
for t in tree:
    while len(t) < 2:
        t.append(0)
jeonwi(1)
x = ''
for i in result:
    x += str(i)+'-'
print(x[:-1])