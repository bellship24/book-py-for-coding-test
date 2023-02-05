'''
- A : 북쪽으로부터 떨어진 칸의 개수
- B : 서쪽으로부터 떨어진 칸의 개수


'''
n, m = map(int, input().split())
x, y, d = map(int, input().split())
array = []
for i in range(n):
    array.append([map(int, input().split())])


directions = [0, 1, 2, 3]


result = 0



print(result)