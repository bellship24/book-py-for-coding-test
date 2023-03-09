# 이진 탐색
n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))


n_list.sort()


def binSearch(array, target, start, end):
    if start > end:
        return "no"

    mid = (start + end) // 2

    if array[mid] == target:
        return "yes"
    elif array[mid] > target:
        return binSearch(array, target, start, mid - 1)
    else:
        return binSearch(array, target, mid + 1, end)
    


for m_i in range(len(m_list)):
    print(binSearch(n_list, m_list[m_i], 0, n-1), end=' ')


'''
5
8 3 7 9 2
3
5 7 9
'''