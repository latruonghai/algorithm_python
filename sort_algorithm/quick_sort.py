from typing import List
from model import Num
from .modules.decorator_for_algorithm import sort_algo


def quick_sort(arr: List[Num], low: int, high: int):
    if low < high:
        pi = partition(arr, low, high)

        quick_sort(arr, pi + 1, high=high)
        quick_sort(arr, low, pi - 1)


def partition(arr: List[Num], low: int, high: int):
    pivot = arr[high]

    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]

    return i + 1
