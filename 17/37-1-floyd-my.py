'''
문제
- 도시(노드) n개 (1 <= n <= 100)
- 버스(간선) m개 (1 <= m <= 100,000)
- 모든 도시의 (A, B) 쌍에 대해 A->B 비용 최솟값을 구하는 프로그램 작성하라

분석
- 모든 도시에서 다른 모든 도시로 최단 경로를 구해야 하며 노드의 갯수가 100개로 적으므로 플로이드 워셜 알고리즘을 활용하는게 적절함.

플로이드 워셜 알고리즘 과정
- 인접 행렬 생성
- 출발지와 도착지가 같은 경우 비용을 0으로 초기화
- 중계지 반복문
    - 출발지 반복문
        - 도착지 반복문
            - 중계지를 거치는게 더 최소 비용인지 확인하고 맞다면 비용을 업데이트
'''

# 노드, 간선 개수 입력 받기
n = int(input())
m = int(input())

# 인접 행렬 생성
INF = int(1e9)
graph = [[INF] * (n+1) for _ in range(n+1)]

# 간선 정보 입력 받기
for _ in range(m):
    start, end, cost = map(int, input().split())
    # 출발지-도착지 간에 간선이 여러개 일수도 있으므로 가장 비용이 적은 간선 정보로 업데이트
    if cost < graph[start][end]:
        graph[start][end] = cost

# 출발지와 도착지가 같은 경우 비용을 0으로 초기화
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0

# 중계지를 거치는게 더 최소 비용인지 확인하고 맞다면 비용을 업데이트
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == INF:
            print(0, end=' ')
        else:
            print(graph[i][j], end=" ")
    print()

'''
5
14
1 2 2
1 3 3
1 4 1
1 5 10
2 4 2
3 4 1
3 5 1
4 5 3
2 5 10
3 1 8
1 4 2
5 1 7
3 4 2
5 2 4

0 2 3 1 4
12 0 15 2 5
8 5 0 1 1
10 7 13 0 3
7 4 10 6 0
'''

