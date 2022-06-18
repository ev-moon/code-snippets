array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = array[0]
    tail = array[1:]
    left_partition = [item for item in tail if item <= pivot]
    right_partition = [item for item in tail if item > pivot]
    return quick_sort(left_partition) + [pivot] + quick_sort(right_partition)


print(quick_sort(array))