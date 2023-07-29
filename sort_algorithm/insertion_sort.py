# Time Complexity of Insertion Sort
# The worst-case time complexity of the Insertion sort is O(N^2)
# The average case time complexity of the Insertion sort is O(N^2)
# The time complexity of the best case is O(N).
# Space Complexity of Insertion Sort
# The auxiliary space complexity of Insertion Sort is O(1)

def insertion_sort(arr, low, high):
    """
     Sorts an array in place using insertion sort. This is a version of the insertion sort used to sort lists of integers

     @param arr - The array to be sorted
     @param low - The lowest value in the array to be sorted
     @param high - The highest value in the array to be sorted
    """
    # Remove all elements from the array.
    for i in range(1, len(arr)):
        key = arr[i]

        j = i - 1
        # Move the key to the next key in the array.
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
