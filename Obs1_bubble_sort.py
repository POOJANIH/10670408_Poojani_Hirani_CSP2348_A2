def obs1_bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        # Track if any swapping happened
        swapped = False
        # Perform the bubble sort for the unsorted portion
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If no swapping happened, array is sorted
        if not swapped:
            break
    return arr
