# # N, M, K를 공백으로 구분하여 입력받기
# n, m, k = map(int, input().split())
# # n : 주어진 수의 개수
# # m : 더할 수 있는 횟수
# # k : 특정 인덱스의 숫자가 더해질 수 있는 최대 횟수

# # N개의 수를 공백으로 구분하여 입력받기
# data = list(map(int, input().split()))

n, m, k = 5, 8, 3
data = [2, 4, 5, 4, 6]

data.sort()  # 입력받은 수 정렬
first = data[-1]
second = data[-2]

# 가장 큰 수가 더해지는 횟수 계산
count = int(m / (k + 1)) * k
count += m % (k + 1)

result = 0
result += count * first
result += (m - count) * second

print(result)

"""
46
"""

# 6+6+6 +5 + 6+6+6 +5 

# 가장 큰 수와 두 번째로 큰 수가 더해질 때 특정한 수열 형태로 반복해서 더해지는 특징이 있음
# 위 예제는 {6+6+6+5}가 반복됨. 이 때, 반복되는 수열의 길이는 (K+1)이 됨.
# 여기서 수열의 반복 횟수 : M // (K+1)
# 여기에 K를 곱해주면 가장 큰 수가 등장하는 횟수 : K * M // (K+1)
# 만약, M이 (K+1)로 나누어 떨어지지 않는 경우 M을 (K+1)로 나눈 나머지 만큼 가장 큰 수가 추가되어 더해짐 : int(M / (K+1)) * K + M % (K+1)