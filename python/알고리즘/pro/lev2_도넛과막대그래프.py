# 입력된 노드 : 나가는 간선이 최소 2개 이상. 들어오는 간선 0개.
# 막대 그래프 : 나가는 간선 0, 들어오는 간선 1 개수. 근데 들어오는 간선이 1개 이상일수도. 추가되는 간선이 끝에 연결될 수 있으니깜.
# 8자 그래프 : 나가는 간선 2, 들어오는 간선 2 개수 근데 들어오는 간선이 2개 이상일수도. 추가되는 간선이 끝에 연결될 수 있으니깜.

def solution(edges):
    answer = [0,0,0,0]
    
    edges_info = dict()
    for a,b in edges:
        if not edges_info.get(a):
            # [나가는 간선, 들어오는 간선]
            edges_info[a] = [0,0]
        if not edges_info.get(b):
            edges_info[b] = [0,0]
        edges_info[a][0] += 1
        edges_info[b][1] += 1
    
    for key in edges_info.keys():
        # 막대
        if edges_info[key][0] == 0 and edges_info[key][1] >= 1:
            answer[2] += 1
        # 8자
        elif edges_info[key][0] == 2 and edges_info[key][1] >= 2:
            answer[3] += 1
        # 추가 노드
        elif edges_info[key][0] >= 2 and edges_info[key][1] == 0:
            answer[0] = key
    # 도넛은 추가된 노드의 간선 수 에서, 8자 그래프와 막대 그래프 수를 빼면 됨.
    # 나이스
    answer[1] = edges_info[answer[0]][0] - answer[2] - answer[3]
            
    
    
    return answer