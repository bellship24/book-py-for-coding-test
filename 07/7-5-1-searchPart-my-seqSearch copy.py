# 순차 탐색
n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

rst = ['no'] * m

for m_i in range(len(m_list)):
    if m_list[m_i] in n_list:
        rst[m_i] = 'yes'


for i in rst:
    print(i, end=' ')

'''
5
8 3 7 9 2
3
5 7 9
'''