n = int(input())

array = []

for i in range(n):
    name_and_score = tuple(input().split())
    array.append(name_and_score)

def setting(data):
    return data[1]

array.sort(key=setting)

for i in range(len(array)):
    print(array[i][0], end=' ')

'''
2
홍길동 95
이순신 77
'''