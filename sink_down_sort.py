def sink_down_sort(arr):
    n = len(arr)
    comparisons = 0
    for i in range(1, n):
        swapped = False
        for j in range(n-1, i-1, -1):
            comparisons += 1
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
                swapped = True
        if not swapped:
            break
    return comparisons

# Test the sink_down_sort function
if __name__ == "__main__":
    import random
    array = [random.randint(1, 100) for _ in range(20)]
    print("Original array:", array)
    comparisons = sink_down_sort(array)
    print("Sorted array:", array)
    print("Number of comparisons:", comparisons)
