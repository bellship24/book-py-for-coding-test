'''
문제
- n, m : 가로, 세로 길이 (1 <= n, m <= 1,000)

분석
- 2차원 그래프 문제.
- 상하좌우에 0이 더 이상 없을 때 까지 탐색하므로 DFS 또는 BFS를 사용할 수 있음.
- BFS 과정
  1. 출발점을 큐에 넣고 방문 처리.
  2. 큐에서 하나 꺼내 인접 노드를 큐에 넣기.
  3. 큐가 빌 때 까지 2번 과정을 반복.
- 이 문제 풀이 방법
  - 모든 노드에 대해 DFS를 수행.


'''

n, m = map(int, input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int, input())))

def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    if graph[x][y] == 0:
        graph[x][y] = 1
        
        dfs(x, y+1)
        dfs(x, y-1)
        dfs(x-1, y)
        dfs(x+1, y)
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1


print(result)

'''
3 3
110
010
101

3
'''