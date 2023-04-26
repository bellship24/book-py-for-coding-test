'''
문제
- 방향 그래프
- 도시 N개 (1<=N<=30,000)
- 통로 M개 (1<=M<=200,000)
- 출발 도시 C (1<=C<=N)
- x 출발, y 도착, z 비용 (1<=x,y,z<=1,000)

- 도시 C에서 메시지를 받게되는 도시의 총 개수는?
- 이 도시들이 모두 메시지를 받는데 까지 걸리는 시간은?

분석
- 한 지점에서 다른 모든 곳으로 가는 최단 경로 문제
- 즉, 다익스트라 알고리즘 문제
- 다익스트라 알고리즘 문제의 풀이 과정
  1. 무한대 값을 갖는 변수 선언
  2. 노드 갯수와 간선 갯수 입력받기
  3. 시작 노드 번호 입력받기
  4. 시작 노드로부터 각 다른 노드들에 대한 최단 거리 테이블 (n+1) 크기의 1차원 리스트
     생성 및 무한대 값 변수로 초기화
  5. 각 인덱스를 출발 노드로, 도착 노드와 비용을 원소로 하는
     간선 그래프 ((n+1), 0) 크기의 2차원 리스트를 선언
  6. 간선 정보를 입력받아 간선 그래프에 업데이트
  7-1. 비용이 0인 시작 노드를 우선순위 큐에 삽입
  7-2. 우선순위 큐에서 비용이 가장 적은 노드를 꺼내기
  7-3. 꺼낸 노드의 인접한 노드들에 대해 꺼낸 노드를 거쳐가는 비용이 기존보다 더 적어진다면
       최단 거리 테이블을 업데이트하고 해당 노드의 간선 정보를 우선순위 큐에 넣기
  7-4. 우선순위 큐가 빌 때 까지 위에 7-2, 7-3번을 반복함
'''

import heapq

INF = int(1e9)

# 도시 개수 N, 통로 개수 M, 출발지 C
n, m, c = map(int, input().split())

distance = [INF] * (n+1)
graph = [[] for _ in range(n+1)]

# 통로 정보
for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

q = []
heapq.heappush(q, (0, c))
distance[c] = 0
while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
        continue
    for ad_node in graph[now]:
        cost = dist + ad_node[1]
        if cost < distance[ad_node[0]]:
            distance[ad_node[0]] = cost
            heapq.heappush(q, (cost, ad_node[0]))

result_node_cnt = 0
result_time = 0

for d in distance:
    if d != INF:
        result_node_cnt += 1
        result_time = max(result_time, d)

print(result_node_cnt-1, result_time)



'''
3 2 1
1 2 4
1 3 2

2 4
'''

