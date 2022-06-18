from typing import List
import itertools


def count_sort(array: List) -> List:
    min_num = min(array)
    max_num = max(array)
    buckets = [0] * (max_num - min_num + 1)
    for item in array:
        buckets[item - min_num] += 1

    # return sum([[min_num + idx] * value for (idx, value) in enumerate(buckets)], [])
    return list(
        itertools.chain.from_iterable(
            [[min_num + idx] * value for (idx, value) in enumerate(buckets)]
        )
    )


array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
print(count_sort(array))