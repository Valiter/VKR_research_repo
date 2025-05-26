def bubble_sort(arr):
    """
    Sorts a list in ascending order using bubble sort algorithm.

    Args:
        arr (list): List of elements to be sorted.

    Returns:
        list: Sorted list.
    """
    n = len(arr)
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap if the element found is greater than the next element
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# Example usage:
reverse_items = [9, 17, 41, 10, 26, 49, 11, 35, 69, 44, 65, 70, 39, 74, 75]
sorted_items = bubble_sort(reverse_items.copy())
print("Sorted list:", sorted_items)

