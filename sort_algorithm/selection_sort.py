from typing import List
from model import Num

# Time Complexity: The time complexity of Selection Sort is O(N2) as there are two nested loops:

# - One loop to select an element of Array one by one = O(N)
# - Another loop to compare that element with every other Array element = O(N)
# - Therefore overall complexity = O(N) * O(N) = O(N*N) = O(N2)


def selection_sort(arr: List[Num], low: int, high: int):
    """
     Sorts an array using selection sort. This is a version of the C - implementation of Python's built - in selection sort.

     @param arr - The array to sort. Must be a list of Num
     @param low - The lowest value to compare.
     @param high - The highest value to compare. If low < high the comparison will be done in place
    """
    # Find the smallest element in the array.
    for i in range(len(arr)):
        min_idx = i
        # Find the minimum index in the array.
        for j in range(i+1, len(arr)):
            # Find the minimum index in the array.
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
