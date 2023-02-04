'''
(실패함)
- 전체 이동 개수에서 불가능한 경우의 수를 빼자
- 전체 개수 : 32 = 상하좌우 2칸 이동(4) * 상하좌우 1칸 이동(4) + 상하좌우 1칸 이동(4) * 상하화주 2칸 이동(4)
- 1단계, 2단계로 나눠서 검토하자
- 1단계 2칸 이동 불가능한 경우 제외
- 1단계 2칸 이동 가능하지만 2단계 1칸 이동 불가능한 경우 제외
- 1단계 1칸 이동 불가능한 경우 제외
- 1단계 1칸 이동 가능하지만 2단계 2칸 이동 불가능한 경우 제외 
'''

here = input()
here_col, here_row = str(here[0]), int(here[1])

cols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
rows = [1, 2, 3, 4, 5, 6, 7, 8]

actions = ['ru', 'rd', 'lu', 'ld']

cant_action_cnt = 0

for action in actions:
    if 'r' in action:
        # 오른쪽 두칸 불가능한 경우
        if cols.index(here_col) >= len(cols) - 2:
            cant_action_cnt += 1

