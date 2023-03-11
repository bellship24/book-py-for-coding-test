n, m = map(int, input().split())
coins = [int(input()) for _ in range(n)]

d = [10001] * m

d[0] = 0

for coin in coins:
    for i in range(len(d)):
        if d[i] % coin == 0:
            d[i] = d[i] // coin




'''
예시
1 : -1

2 : 1
2

3 : 1
3

4 : 2
2
2

5 : 2
3
2

6 : 2
3
3

7 : 3
3
2
2

'''

'''
점화식
an = min

'''

'''
2 15
2
3
'''