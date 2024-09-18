def obs3_bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        # Only scan the first n-i-1 elements
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr
