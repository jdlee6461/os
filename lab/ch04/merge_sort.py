from concurrent.futures import ProcessPoolExecutor
import random
import sys
import time

PROCESS_NUM = 2

def merge(left, right):
    left_length, right_length = len(left), len(right)
    left_index, right_index = 0, 0
    merged = []
    while left_index < left_length and right_index < right_length:
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    if left_index == left_length:
        merged.extend(right[right_index:])
    else:
        merged.extend(left[left_index:])
    return merged


def merge_sort(data):
    length = len(data)
    if length <= 1:
        return data
    middle = int(length / 2)
    left = merge_sort(data[:middle])
    right = merge_sort(data[middle:])
    return merge(left, right)


def merge_sort_parallel(data):
    """Do your job here!
    """
    pass


if __name__ == "__main__":
    size = int(sys.argv[1])
    data_unsorted = [random.randint(0, size) for _ in range(size)]
    
    for sort in [merge_sort, merge_sort_parallel]:
        start = time.time()
        data_sorted = sort(data_unsorted)
        end = time.time() - start
        print(sort.__name__, end, sorted(data_unsorted) == data_sorted)