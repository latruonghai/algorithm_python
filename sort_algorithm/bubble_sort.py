from model import Num
from typing import List


def bubble_sort(arr: List[Num], low: int, high: int):
    """
     Bubble sort the array using the algorithm. It is used to sort the data in ascending order.

     @param arr - The array to be sorted. Should be a list
     @param low - The lower bound of the sort interval.
     @param high - The upper bound of the sort interval. This is a function
    """
    n = len(arr)
    # This function is used to sort the array by the largest element in the array.
    for i in range(0, n-1):
        # Remove the largest element of the array.
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]


# This function is called by the test case sort algorithm.
if __name__ == "__main__":

    with open("test_cases/test_case_sort_algorithm1.txt", "r") as file:
        result = file.read()
        arr = result.split()
    bubble_sort(arr)
    # print('arr: ', arr)
