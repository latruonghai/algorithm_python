import time

from .modules.decorator_for_algorithm import sort_algo


@sort_algo
def bubble_sort(arr, low, high):
    n = len(arr)
    for i in range(0, n-1):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]


if __name__ == "__main__":

    with open("test_cases/test_case_sort_algorithm1.txt", "r") as file:
        result = file.read()
        arr = result.split()
    bubble_sort(arr)
    # print('arr: ', arr)
