'''
실패
'''

n, m = map(int, input().split())
h_list = list(map(int, input().split()))

def binarySearch(array, target, start, end):

    while start <= end:
        mid = (start + end) // 2
        sliced_h_list = [x - mid if x > mid else 0 for x in h_list]

        print(mid)

        if m == sum(sliced_h_list):
            return mid
        elif m < sum(sliced_h_list):
            start = mid + 1
        else:
            end = mid - 1
    


    return mid


print(binarySearch(h_list, m, 0, max(h_list)))



'''
4 6
19 15 10 17
'''