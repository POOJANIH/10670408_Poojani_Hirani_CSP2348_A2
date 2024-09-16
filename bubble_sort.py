def bubble_sort(arr):
    n = len(arr)
    comparisons = 0  # Track the number of comparisons
    swaps = 0  # Track the number of swaps
    
    # Outer loop for each pass
    for i in range(n):
        swapped = False
        # Inner loop to compare adjacent elements
        for j in range(n - i - 1):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                # Swap elements if they're in the wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
                swapped = True
        # If no elements were swapped in the inner loop, the array is sorted
        if not swapped:
            break
    
    return comparisons, swaps

# Testing with an array of 20 random elements
if __name__ == "__main__":
    import random
    
    # Generate a random array of 20 integers between 1 and 100
    arr = [random.randint(1, 100) for _ in range(20)]
    print("Original array:", arr)
    
    comparisons, swaps = bubble_sort(arr)
    
    print("Sorted array:", arr)
    print(f"Total comparisons: {comparisons}")
    print(f"Total swaps: {swaps}")
