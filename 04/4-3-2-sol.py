'''
로직
- 나이트의 이동 경로를 step 변수로 표현하고 각 원소를 튜플로 정의함.
- 그 후, 나이트의 현재 위치에서 step들을 적용함.
- 결과값이 8 x 8 좌표에 있는지 확인하자.

기타
- a, b, c, d, ...로 받는 문자열을 좌표로 사용할 때는 int(ord('a'))와 같은 방법으로 숫자 좌표로 변환 가능함.
'''


# 현재 나이트의 위치 입력받기
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1


# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2, -1), (-1, -2),
         (-2, 1), (-1, 2),
         (2, -1), (1, -2),
         (2, 1), (1, 2)
         ]


# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0
for step in steps:
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_column = column + step[1]
    # 해당 위치로 이동이 가능하다면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)