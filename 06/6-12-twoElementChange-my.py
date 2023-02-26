n, k = map(int, input().split())
array_a = list(map(int, input().split()))
array_b = list(map(int, input().split()))

array_a.sort()
array_b.sort(reverse=True)

for i in range(k):
    array_a[i], array_b[i] = array_b[i], array_a[i]

sum = 0
for i in array_a:
    sum += i

print(sum)


'''
5 3
1 2 5 4 3
5 5 6 6 5
'''