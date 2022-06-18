from typing import List


def insertion_sort(input_list: List) -> List:
    for i in range(1, len(input_list)):
        for j in range(i, 0, -1):
            if input_list[j] < input_list[j - 1]:
                input_list[j], input_list[j - 1] = input_list[j - 1], input_list[j]
    return input_list


input_list = list(map(int, input().split()))
print(insertion_sort(input_list))