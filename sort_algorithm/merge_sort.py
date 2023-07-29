from typing import List
from model import Num

# Time Complexity: O(N log(N)),  Merge Sort is a recursive algorithm and time complexity can be expressed as following recurrence relation.
# Auxiliary Space: O(N), In merge sort all elements are copied into an auxiliary array. So N auxiliary space is required for merge sort.


def merge_sort(arr: List[Num], low: int, high: int):
    """
     Mergesort a list of Num into a sorted list. The merge sort is used to find the longest subsequence that is greater than or equal to the low and high parameters

     @param arr - The list to be sorted
     @param low - The lowest index of the subsequence to be sorted
     @param high - The highest index of the subsequence to be
    """
    # sort the array by the smallest element in the list
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L, low, high)
        merge_sort(R, low, high)
        i = j = k = 0

        # Move the elements of L and R to the largest element in the list L and R.
        while i < len(L) and j < len(R):
            # Move the first element of the list to the right of the list.
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        # Copy the L elements of the list L into arr.
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        # Copy the R array to the receiver.
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
