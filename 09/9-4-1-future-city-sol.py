'''
문제
- 노드는 N 개. 경로는 M 개 (1<= N, M <=100)
- 현재 위치 1 에서 X로 이동.
- 무방향.
- 간선의 비용은 모두 1.
- 이동 경로 : 1번 회사 -> K -> X.
- 이동 최소 시간을 계산하라.

분석
- 노드 개수 N은 100개 미만으로 적어서 플로이드 워셜 알고리즘이 가능하며 구현이 쉬우므로 바람직함.
- 간선의 비용은 모두 1이므로 이동 간에 거치는 노드가 적을수록 최단거리임.
- 1 -> K 최단거리 비용을 구하고 K -> X 최단거리 비용을 구해서 더하자.
- 이 방법은 점화식으로 쓸 수 있고 다이나믹 프로그래밍이 될 수 있으며 플루이드 워셜 알고리즘을 사용할 수 있음.
'''

# 무한을 의미하는 값으로 10억을 설정
INF = int(1e9)

# 노드의 개수 및 간선의 개수를 입력받기
n, m = map(int, input().split())

# 2 차원 리스트(그래프 표현)를 만들고 모든 값을 무한으로 초기화
graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# 거쳐 갈 노드 X와 최종 목적지 노드 K를 입력받기
x, k = map(int, input().split())

# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행된 결과를 출력
distance = graph[1][k] + graph[k][x]

if distance >= INF:
    print("-1")
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
