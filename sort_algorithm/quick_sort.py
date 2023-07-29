from typing import List
from model import Num
from .modules.decorator_for_algorithm import sort_algo

# Time Complexity:

# Best Case: \omega (N * log N)
# Average Case: \Theta (N * logN)
# Worst Case: O(N2)


def quick_sort(arr: List[Num], low: int, high: int):
    """
    Sort an array using quicksort. This is a destructive sort and will preserve the order of the array

     @param arr - The array to be sorted
     @param low - The lowest index of the array ( inclusive )
     @param high - The highest index of the array ( inclusive )
    """
    # Sort the array by the smallest element in the array.
    if low < high:
        pi = partition(arr, low, high)

        quick_sort(arr, pi + 1, high=high)
        quick_sort(arr, low, pi - 1)


def partition(arr: List[Num], low: int, high: int):
    """
     Partition the array so that the pivot is at the beginning of the array. This is useful for sorting a list of numbers in ascending order

     @param arr - The array to be partitioned
     @param low - The index of the first element in the partition
     @param high - The index of the last element in the partition

     @return The index of the pivot that was used to partition the array in ascending order i. e. the first element greater than
    """
    pivot = arr[high]

    i = low - 1

    # Swap the pivot value of the array
    for j in range(low, high):
        # Move the pivot to the pivot.
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]

    return i + 1
