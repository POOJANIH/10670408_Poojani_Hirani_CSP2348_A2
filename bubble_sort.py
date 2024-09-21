#Author : P S Minoli Hirani
# Date : 17/09/2024

import random
import time

# Basic Bubble Sort
def bubble_sort(arr):
    comparisons = 0
    swaps = 0
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            comparisons += 1  # Count the comparison
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1  # Count the swap
    return arr, comparisons, swaps

# Observation 1 - Reduce unnecessary comparisons
def obs1_bubble_sort(arr):
    comparisons = 0
    swaps = 0
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            comparisons += 1  # Count the comparison
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1  # Count the swap
    return arr, comparisons, swaps

# Observation 2 - Stop if no swaps are made (array is already sorted)
def obs2_bubble_sort(arr):
    comparisons = 0
    swaps = 0
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            comparisons += 1  # Count the comparison
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1  # Count the swap
                swapped = True
        if not swapped:
            break
    return arr, comparisons, swaps

# Observation 3 - Combines both Obs1 and Obs2
def obs3_bubble_sort(arr):
    comparisons = 0
    swaps = 0
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            comparisons += 1  # Count the comparison
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1  # Count the swap
                swapped = True
        if not swapped:
            break
    return arr, comparisons, swaps

def sink_down_sort(arr):
    comparisons = 0
    swaps = 0
    n = len(arr)
    
    for i in range(n):
        for j in range(n - 1, i, -1):  # Start from the end and move to the start
            comparisons += 1
            if arr[j] < arr[j - 1]:  # Swap if elements are out of order
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                swaps += 1
                
    return arr, comparisons, swaps

def improved_sink_down_sort(arr):
    comparisons = 0
    swaps = 0
    n = len(arr)
    
    for i in range(n):
        swapped = False
        for j in range(n - 1, i, -1):  # Start from the end and move to the start
            comparisons += 1
            if arr[j] < arr[j - 1]:  # Swap if elements are out of order
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                swaps += 1
                swapped = True
        if not swapped:  # Exit if no swaps occurred
            break
            
    return arr, comparisons, swaps

# Bi-directional Bubble Sort
def bi_directional_bubble_sort(arr):
    comparisons = 0
    swaps = 0
    n = len(arr)
    left = 0
    right = n - 1
    while left < right:
        # Left to right scan (bubble up)
        for i in range(left, right):
            comparisons += 1  # Count the comparison
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swaps += 1  # Count the swap
        right -= 1
        # Right to left scan (sink down)
        for i in range(right, left, -1):
            comparisons += 1  # Count the comparison
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                swaps += 1  # Count the swap
        left += 1
    return arr, comparisons, swaps

# Test the sorting algorithms
def test_sorting_algorithms():
    random_array = [random.randint(1, 100) for _ in range(20)]
    print("Original Array:", random_array)

    # Basic Bubble Sort
    start = time.time()
    sorted_basic, comparisons_basic, swaps_basic = bubble_sort(random_array[:])
    end = time.time()
    print("\nBasic Bubble Sort:", sorted_basic)
    print("Comparisons:", comparisons_basic, "Swaps:", swaps_basic, "Time:", end - start, "seconds")

    # Obs1-BubbleSort
    start = time.time()
    sorted_obs1, comparisons_obs1, swaps_obs1 = obs1_bubble_sort(random_array[:])
    end = time.time()
    print("\nObs1 Bubble Sort (Reduced Comparisons):", sorted_obs1)
    print("Comparisons:", comparisons_obs1, "Swaps:", swaps_obs1, "Time:", end - start, "seconds")

    # Obs2-BubbleSort
    start = time.time()
    sorted_obs2, comparisons_obs2, swaps_obs2 = obs2_bubble_sort(random_array[:])
    end = time.time()
    print("\nObs2 Bubble Sort (Early Exit):", sorted_obs2)
    print("Comparisons:", comparisons_obs2, "Swaps:", swaps_obs2, "Time:", end - start, "seconds")

    # Obs3-BubbleSort
    start = time.time()
    sorted_obs3, comparisons_obs3, swaps_obs3 = obs3_bubble_sort(random_array[:])
    end = time.time()
    print("\nObs3 Bubble Sort (Reduced Comparisons + Early Exit):", sorted_obs3)
    print("Comparisons:", comparisons_obs3, "Swaps:", swaps_obs3, "Time:", end - start, "seconds")

    # Sink-Down Sort (Basic)
    start = time.time()
    sorted_sink, comparisons_sink, swaps_sink = sink_down_sort(random_array[:])
    end = time.time()
    print("\nBasic Sink-Down Sort:", sorted_sink)
    print("Comparisons:", comparisons_sink, "Swaps:", swaps_sink, "Time:", end - start, "seconds")

    # Improved Sink-Down Sort
    start = time.time()
    sorted_sink_improved, comparisons_sink_improved, swaps_sink_improved = improved_sink_down_sort(random_array[:])
    end = time.time()
    print("\nImproved Sink-Down Sort:", sorted_sink_improved)
    print("Comparisons:", comparisons_sink_improved, "Swaps:", swaps_sink_improved, "Time:", end - start, "seconds")

    # Bi-Directional Bubble Sort
    start = time.time()
    sorted_bdb, comparisons_bdb, swaps_bdb = bi_directional_bubble_sort(random_array[:])
    end = time.time()
    print("\nBi-Directional Bubble Sort:", sorted_bdb)
    print("Comparisons:", comparisons_bdb, "Swaps:", swaps_bdb, "Time:", end - start, "seconds")

# Run the test
test_sorting_algorithms()
