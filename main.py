from sort_algorithm import *
from sort_algorithm.modules.decorator_for_algorithm import sort_algo

if __name__ == "__main__":
    sort_algorithm = [quick_sort, bubble_sort]
    with open("sort_algorithm/test_cases/test_case_sort_algorithm1.txt", "r") as file:
        result = file.read()
        arr = result.split()
    for algorithm in sort_algorithm:
        sort_algo(algorithm)(arr, 0, len(arr)-1)
