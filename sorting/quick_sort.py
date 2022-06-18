array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(array, start, end):
    if start >= end:
        return
    pivot = start
    l_point = start + 1
    r_point = end
    while l_point <= r_point:
        while l_point <= end and array[l_point] <= array[pivot]:
            l_point += 1
        while r_point > start and array[r_point] >= array[pivot]:
            r_point -= 1
        if l_point > r_point:
            array[r_point], array[pivot] = array[pivot], array[r_point]
        else:
            array[l_point], array[r_point] = array[r_point], array[l_point]
    quick_sort(array, start, r_point - 1)
    quick_sort(array, r_point + 1, end)


quick_sort(array, 0, len(array) - 1)
print(array)