from model import Num
from typing import List

# Time Complexity: O(N log N)
# Auxiliary Space: O(log n), due to the recursive call stack. However, auxiliary space can be O(1) for iterative implementation.


def heapify(arr: List[Num], N: int, i: int):
    """
     Sort the array by heapifying the elements at the given index. This is a recursive function.

     @param arr - The array to be sorted. It must be a list of length N
     @param N - The length of the array
     @param i - The index of the element to
    """
    largest = i
    l = i*2+1
    r = i*2+2

    # Find the largest element in the array.
    if l < N and arr[l] > arr[largest]:
        largest = l
    # Find the largest element in the array.
    if r < N and arr[r] > arr[largest]:
        largest = r
    # heapify arr i largest i
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, N, largest)


def heap_sort(arr, N, i):
    """
     Heap sort of a 1D array. It is used to sort an N - dimensional array by heapify ( in - place )

     @param arr - The array to be sorted
     @param N - The number of elements in the array that will be sorted
     @param i - The index of the element to be sorted ( 0 for the first element
    """
    # heapify arr N 2 1 1 1 1
    for i in range(N//2-1, -1, -1):
        heapify(arr, N, i)
    # heapify arr N 1 1 1 1 1 1
    for i in range(N-1, -1, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
