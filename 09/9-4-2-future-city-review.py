'''
프로이드 워셜 알고리즘 과정
- 무한대 값을 갖는 변수 만들기
- 노드 갯수와 간선 갯수 입력받기
- 비용 그래프 용도로 (노드 갯수 * 노드 갯수) 크기의 2차원 배열 만들고 값은 무한대 값 변수로 초기화하기
- 그래프의 각 원소들을 반복문으로 돌면서 출발지와 도착지가 같은 노드에 대해 비용을 0으로 초기화하기
- 간선의 갯수만큼 간선 정보를 입력받고 비용 그래프에 초기화하기
- 플로이드 워셜 알고리즘 수행
  - 경유지, 출발지, 도착지를 각 노드에 대해 3중 반복문을 돌면서
    출발지->도착지 방법 혹은 출발지->경유지->도착지 방법 중에 비용이 최소화 되는 방법으로 그래프를 업데이트하기
'''

INF = int(1e9)

n, m = map(int, input().split())

graph = [[INF] * (n+1) for _ in range(n+1)]

for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, input().split())

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[b][k])

distance = graph[1][k] + graph[k][x]

if distance >= INF:
    print('-1')
else:
    print(distance)

'''
5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5

3
'''

'''
4 2
1 3
2 4
3 4

-1
'''
