import heapq

INF = int(1e9)

n, m = map(int, input().split())
start = int(input())

distance = [INF] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    start_node, end_node, cost = map(int, input().split())
    graph[start_node].append((end_node, cost))

q = []

heapq.heappush(q, (0, start))
distance[start] = 0

while q:
    now_cost, now_node = heapq.heappop(q)
    if distance[now_node] < now_cost:
        continue
    distance[now_node] = now_cost
    for adj_node, adj_cost in graph[now_node]:
        print(f"now_node {now_node}'s adjacent ({adj_cost}, {adj_node})")
        # break

        # 출발-현재 비용 + 현재-인접 비용
        via_cost = now_cost + adj_cost

        if via_cost < distance[adj_node]:
            distance[adj_node] = via_cost
            heapq.heappush(q, (via_cost, adj_node))

for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])




'''
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2

0
2
3
1
2
4
'''
