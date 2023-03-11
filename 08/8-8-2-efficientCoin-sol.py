# 정수 N, M 입력받기
n, m = map(int, input().split())
# N개의 화폐 단위 정보를 입력받기
array = [int(input()) for _ in range(n)]


# 한 번 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [10001] * (m + 1)


# 다이나믹 프로그래밍 진행 (바텀업)
d[0] = 0
for i in range(n):
    for j in range(array[i], m + 1):
        if d[j - array[i]] != 10001:  # (i - k)원을 만드는 방법이 존재하는 경우
            d[j] = min(d[j], d[j - array[i]] + 1)


# 계산된 결과 출력
if d[m] == 10001:  # 최종적으로 M원을 만드는 방법이 없는 경우
    print(-1)
else:
    print(d[m])


'''
점화식
- a_{i-k} 를 만드는 방법이 존재하는 경우, a_i = min(a_i, a_{i-k}+1)
- a_{i-k} 를 만드는 방법이 존재하지 않는 경우, a_i = 10001
'''

'''
2 15
2
3

5
'''


'''
3 4
3
5
7

-1
'''