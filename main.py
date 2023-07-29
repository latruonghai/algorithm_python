from sort_algorithm import *
from sort_algorithm.modules.decorator_for_algorithm import sort_algo
import random
if __name__ == "__main__":
    sort_algorithm = [quick_sort, bubble_sort,
                      insertion_sort, selection_sort, merge_sort, heap_sort]
    arr_sample = [random.randint(150, 10000) for _ in range(100000)]
    # print('pre_sorted_arr: ', arr_sample)
    # with open("sort_algorithm/test_cases/test_case_sort_algorithm1.txt", "r") as file:
    #     result = file.read()
    #     arr = result.split()
    for algorithm in sort_algorithm:
        arr = arr_sample.copy()
        sort_algo(algorithm)(arr, 0, len(arr)-1)
        # print('sorted_arr: ', arr)
