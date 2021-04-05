'''
이진탐색트리의 생성 연산을 구현하세요!
모든 연산 수행 후의 이진탐색트리를 전위운행(preorder) 수행해서 출력합니다.

8 <- 초기 생성할 노드 개수
9 4 3 6 12 15 13 17  <- 초기 생성할 노드의 값


* 노드 탐색, 전위운행(preorder)에 대한 함수도 생성합니다.
각 기능은 함수로 작성하도록 합니다.

생성 후 Tree의 모습

'''


import sys
sys.stdin = open("tree03_input.txt")


def make_node(root, x):
    if root > x:
        if left[node_list.index(root)]:
            make_node(left[node_list.index(root)], x)
        else:
            left[node_list.index(root)] = x
    else:
        if right[node_list.index(root)]:
            make_node(right[node_list.index(root)], x)
        else:
            right[node_list.index(root)] = x


# 처음 x 값 = 9
def preorder(x):
    if x:
        result.append(x)
        preorder(left[node_list.index(x)])
        preorder(right[node_list.index(x)])

node_num = int(input())
node_list = list(map(int, input().split()))

root = node_list[0]
left = [0] * node_num
right = [0] * node_num
for i in range(1, node_num):
    make_node(root, node_list[i])
# print(left)
# print(right)
result = []
preorder(root)
print('-'.join(map(str, result)))
