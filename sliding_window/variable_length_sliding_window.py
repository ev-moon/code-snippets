# Returns maximum length of subarray with sum less than k.


def get_max_subarray_sum(array: list, k: int):
    start = 0
    cur_sum = 0
    max_subarray_length = 0
    for idx, num in enumerate(array):
        cur_sum += num
        while cur_sum > k:
            cur_sum -= array[start]
            start += 1
        max_subarray_length = max(max_subarray_length, idx - start + 1)
    return max_subarray_length


nums = [1, 2, 3, 4, 5]
k = 11
print(get_max_subarray_sum(nums, k))
