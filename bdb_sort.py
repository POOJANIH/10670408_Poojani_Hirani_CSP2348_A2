def bdb_sort(arr):
    n = len(arr)
    comparisons = 0
    for i in range(n//2):
        # Left-to-right scan
        for j in range(n-i-1):
            comparisons += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
        # Right-to-left scan
        for k in range(n-i-2, i-1, -1):
            comparisons += 1
            if arr[k] > arr[k+1]:
                arr[k], arr[k+1] = arr[k+1], arr[k]
    return comparisons

# Test the bdb_sort function
if __name__ == "__main__":
    import random
    array = [random.randint(1, 100) for _ in range(20)]
    print("Original array:", array)
    comparisons = bdb_sort(array)
    print("Sorted array:", array)
    print("Number of comparisons:", comparisons)
