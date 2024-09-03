# Returns the maximum sum of a subarray for a given length.


def get_max_subarray_sum(array: list, subarray_length: int):
    if len(array) < subarray_length:
        print("Array cannot be shorter than subarray.")
        return
    cur_subarray_sum = sum(array[:subarray_length])
    max_subarray_sum = cur_subarray_sum
    for i in range(subarray_length, len(array)):
        cur_subarray_sum += array[i] - array[i - subarray_length]
        max_subarray_sum = max(max_subarray_sum, cur_subarray_sum)
    return max_subarray_sum


nums = [2, 1, 5, 1, 3, 2]
window_size = 3
print(get_max_subarray_sum(nums, 3))
