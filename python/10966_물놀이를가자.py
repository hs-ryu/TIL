'''
여름이 되어 물놀이를 가는 사람들이 많다. 
지도는 N×M크기의 격자로 표현이 가능하고, 위쪽에서 i번째 줄의 왼쪽에서 j번째 칸이 물이면 ‘W’, 땅이면 ‘L’로 표현된다. 
어떤 칸에 사람이 있으면, 그 칸의 상하좌우에 있는 칸으로 이동하는 것을 반복하여 다른 칸으로 이동할 수 있다.
 단, 격자 밖으로 나가는 이동은 불가능하다. 
 땅으로 표현된 모든 칸에 대해서, 어떤 물인 칸으로 이동하기 위한 최소 이동 횟수를 구하고 모든 이동 횟수의 합을 출력하는 프로그램을 작성하라.

 

[입력]

첫 번째 줄에 테스트 케이스의 수 가 주어진다.
 

각 테스트 케이스의 첫 번째 줄에는 두 정수 이 공백 하나로 구분되어 주어진다.

다음 개의 줄에는 길이 인 문자열이 주어진다. 문자열은 ‘W’또는 ‘L’로만 이루어져 있다. 
모든 줄의 문자열을 모두 합쳤을 때, 적어도 하나의 ‘W’는 주어지는 것이 보장된다.

 

[출력]
 

각 테스트 케이스마다 땅으로 표현된 모든 칸에 대해서, 물인 칸으로 이동하기 위한 최소 이동 횟수의 합을 출력한다.
'''












# 아이디어1. 모든 땅에서 가장 가까운 물을 찾는다.  -> ????
# 물에서 각 땅에 대한 최단 거리를 찾는 경우  -> 물에서 출발하는 BFS
# 물이 여러개면 여러개 시작점