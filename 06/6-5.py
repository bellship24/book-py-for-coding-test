def quick_sort(array):
    if len(array) <= 1:
        return array
    
    pivot = array[0]
    tail = array[1:]
    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]


    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

array = [1, 2, 6, 4, 3, 9, 7, 8, 5]
print(quick_sort(array))

