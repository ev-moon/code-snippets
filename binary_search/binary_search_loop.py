def binary_search(array, target):
    start = 0
    end = len(array) - 1

    while True:
        if start > end:
            return None
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1


target = int(input())
array = list(map(int, input().split()))

result = binary_search(array, target)
print(result)
