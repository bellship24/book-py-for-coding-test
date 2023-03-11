# 해설 읽고 풀음
n = int(input())
k_list = list(map(int, input().split()))

d = [0] * n
d[0] = k_list[0]
if n >= 2:
    d[1] = max(k_list[0], k_list[1])

for i in range(2, n):
    d[i] = max(d[i - 2] + k_list[i], d[i - 1])

print(d[n-1])

'''
4
1 3 1 5

8
'''