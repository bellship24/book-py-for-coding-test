'''
N : (노드) 마을의 집
M : (간선) 집들을 연결하는 길

무방향 간선

유지비 : 간선의 비용

집들이 있는 마을을 2개로 분리할 계획
각 분리된 마을 안에 집들은 서로 연결되도록 분할해야 함 = 마을 안에 임의의 두 집 사이에 경로가 항상 존재해야 함

마을에는 집이 1개 이상 있어야 함

분리된 마을 간에는 길이 없어야 함

각 마을 안에서도 임의의 두 집 사이에 경로가 항상 존재하게 하면서 길을 더 없앨 수 있음.(?)

위 조건들을 만족하면서 유지비의 합을 최소로 하기
'''

n, m = map(int, input().split())

edges = []

for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

edges.sort(key=lambda x: x[2])

parent = [i for i in range(n + 1)]

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

result = 0

for i, edge in edges:
    a, b, c = edge

    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += c
        last = c

print(result - last)

'''
7 12
1 2 3
1 3 2
3 2 1
2 5 2
3 4 4
7 3 6
5 1 5
1 6 2
6 4 1
6 5 3
4 5 3
6 7 4


8
'''