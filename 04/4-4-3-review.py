n, m = map(int, input().split())
a, b, d = map(int, input().split())
total_map = [list(map(int, input().split())) for _ in range(n)]

arrived = [[0] * m for _ in range(n)]

# 북/동/남/서 방향에 따른 이동
arrived_a_list = [-1, 0, 1, 0]
arrived_b_list = [0, 1, 0, -1]

def turn_left():
    global d
    d -= 1
    if d == -1:
        d = 3

arrived[a][b] = 1

count = 0
turn_time = 0

while True:
    turn_left()
    next_a = a + arrived_a_list[d]
    next_b = b + arrived_b_list[d]
    
    if arrived[next_a][next_b] == 0 and total_map[next_a][next_b] == 0:
        a = next_a
        b = next_b
        arrived[next_a][next_b] = 1
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1
    if turn_time == 4:
        next_a = a - arrived_a_list[d]
        next_b = b - arrived_b_list[d]
        if arrived[next_a][next_b] == 0:
            a = next_a
            b = next_b
            turn_time = 0
        else:
            break

print(count)

