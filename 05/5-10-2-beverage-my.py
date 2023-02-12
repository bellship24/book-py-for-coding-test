n, m = map(int, input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int, input())))


def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if graph[x][y] == 0:
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j):
            result += 1

print(result)






'''
로직
- 상, 하, 좌, 우로 연결되어 있는 공간은 그래프로 표현할 수 있음.
- 그래프에서 묶음의 개수를 구하기 위해서 DFS를 이용할 수 있음.

기타
- list()와 []의 차이 : list()는 input을 각 원소로 쪼개고 []는 input을 하나의 원소로 사용함.
'''