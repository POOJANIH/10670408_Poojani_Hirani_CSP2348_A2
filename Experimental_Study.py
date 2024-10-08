#Author : P S Minoli Hirani
# Date : 17/09/2024

import random
import time

# Sorting algorithms implementations
def bubble_sort(arr):
    comparisons = 0
    swaps = 0
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
    return comparisons, swaps

def obs1_bubble_sort(arr):
    comparisons = 0
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return comparisons, 0  # Swaps not counted

def obs2_bubble_sort(arr):
    comparisons = 0
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return comparisons, 0

def obs3_bubble_sort(arr):
    comparisons = 0
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return comparisons, 0

def sink_down_sort(arr):
    comparisons = 0
    n = len(arr)
    for i in range(n):
        for j in range(n - 1, i, -1):
            comparisons += 1
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
    return comparisons, 0

def bi_directional_bubble_sort(arr):
    comparisons = 0
    n = len(arr)
    left, right = 0, n - 1
    while left < right:
        for i in range(left, right):
            comparisons += 1
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        right -= 1
        for i in range(right, left, -1):
            comparisons += 1
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
        left += 1
    return comparisons, 0

def selection_sort(arr):
    comparisons = 0
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            comparisons += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return comparisons, 0  # Swaps not counted

def insertion_sort(arr):
    comparisons = 0
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            comparisons += 1
            arr[j + 1] = arr[j]
            j -= 1
        comparisons += 1  # Last comparison
        arr[j + 1] = key
    return comparisons, 0  # Swaps not counted

def merge_sort(arr):
    comparisons = 0
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        comparisons += merge_sort(L)
        comparisons += merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            comparisons += 1
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

    return comparisons

def quick_sort(arr):
    comparisons = 0
    if len(arr) <= 1:
        return arr, comparisons
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x <= pivot]
        right = [x for x in arr[1:] if x > pivot]
        comparisons += len(arr) - 1 + quick_sort(left)[1] + quick_sort(right)[1]
        return left + [pivot] + right, comparisons

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    comparisons = 0

    if left < n and arr[left] > arr[largest]:
        largest = left
        comparisons += 1

    if right < n and arr[right] > arr[largest]:
        largest = right
        comparisons += 1

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        comparisons += heapify(arr, n, largest)

    return comparisons

def heap_sort(arr):
    n = len(arr)
    comparisons = 0

    for i in range(n // 2 - 1, -1, -1):
        comparisons += heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        comparisons += heapify(arr, i, 0)

    return comparisons

# Function to conduct the experimental study
def conduct_experiment(sizes):
    results_comparisons = {}
    results_time = {}

    # Run each algorithm for each size
    for size in sizes:
        comparisons_total = {
            "Selection": 0,
            "Insertion": 0,
            "Merge": 0,
            "Quick": 0,
            "Heap": 0,
            "Bubble": 0,
            "Obs1-Bubble": 0,
            "Obs2-Bubble": 0,
            "Obs3-Bubble": 0,
            "Sink-Down": 0,
            "Bi-Directional": 0,
        }
        time_total = {key: 0 for key in comparisons_total.keys()}

        for _ in range(10):  # Average over 10 runs
            random_array = [random.randint(1, 1000) for _ in range(size)]

            # Measure Bubble Sort
            start_time = time.time()
            comparisons, _ = bubble_sort(random_array[:])
            end_time = time.time()
            comparisons_total["Bubble"] += comparisons
            time_total["Bubble"] += (end_time - start_time) * 1000  # Convert to milliseconds

            # Measure Selection Sort
            start_time = time.time()
            comparisons, _ = selection_sort(random_array[:])
            end_time = time.time()
            comparisons_total["Selection"] += comparisons
            time_total["Selection"] += (end_time - start_time) * 1000

            # Measure Insertion Sort
            start_time = time.time()
            comparisons, _ = insertion_sort(random_array[:])
            end_time = time.time()
            comparisons_total["Insertion"] += comparisons
            time_total["Insertion"] += (end_time - start_time) * 1000

            # Measure Merge Sort
            start_time = time.time()
            comparisons = merge_sort(random_array[:])
            end_time = time.time()
            comparisons_total["Merge"] += comparisons
            time_total["Merge"] += (end_time - start_time) * 1000

            # Measure Quick Sort
            start_time = time.time()
            _, comparisons = quick_sort(random_array[:])
            end_time = time.time()
            comparisons_total["Quick"] += comparisons
            time_total["Quick"] += (end_time - start_time) * 1000

            # Measure Heap Sort
            start_time = time.time()
            comparisons = heap_sort(random_array[:])
            end_time = time.time()
            comparisons_total["Heap"] += comparisons
            time_total["Heap"] += (end_time - start_time) * 1000

            # Measure Obs1-Bubble Sort
            start_time = time.time()
            comparisons, _ = obs1_bubble_sort(random_array[:])
            end_time = time.time()
            comparisons_total["Obs1-Bubble"] += comparisons
            time_total["Obs1-Bubble"] += (end_time - start_time) * 1000

            # Measure Obs2-Bubble Sort
            start_time = time.time()
            comparisons, _ = obs2_bubble_sort(random_array[:])
            end_time = time.time()
            comparisons_total["Obs2-Bubble"] += comparisons
            time_total["Obs2-Bubble"] += (end_time - start_time) * 1000

            # Measure Obs3-Bubble Sort
            start_time = time.time()
            comparisons, _ = obs3_bubble_sort(random_array[:])
            end_time = time.time()
            comparisons_total["Obs3-Bubble"] += comparisons
            time_total["Obs3-Bubble"] += (end_time - start_time) * 1000

            # Measure Sink-Down Sort
            start_time = time.time()
            comparisons, _ = sink_down_sort(random_array[:])
            end_time = time.time()
            comparisons_total["Sink-Down"] += comparisons
            time_total["Sink-Down"] += (end_time - start_time) * 1000

            # Measure Bi-Directional Bubble Sort
            start_time = time.time()
            comparisons, _ = bi_directional_bubble_sort(random_array[:])
            end_time = time.time()
            comparisons_total["Bi-Directional"] += comparisons
            time_total["Bi-Directional"] += (end_time - start_time) * 1000

        # Average results
        for key in comparisons_total:
            comparisons_total[key] /= 10
            time_total[key] /= 10

        results_comparisons[size] = comparisons_total
        results_time[size] = time_total

    return results_comparisons, results_time

# Define the sizes to test
sizes_to_test = [100, 200, 400, 800, 1000, 2000]

# Conduct the experiment
average_comparisons, average_time = conduct_experiment(sizes_to_test)

# Print the results in the specified table format
print("Table 2: Experimental study: Average number of comparisons for sorting arrays of n integers (over 10 runs).")
print("Sorting Algorithm | n=100 | n=200 | n=400 | n=800 | n=1000 | n=2000")
for algo in average_comparisons[sizes_to_test[0]].keys():
    results = [f"{average_comparisons[size][algo]:.2f}" for size in sizes_to_test]
    print(f"{algo:<18} | {' | '.join(results)}")

print("\nTable 3: Experimental study: Average running time (in ms) for sorting arrays of n integers (over 10 runs).")
print("Sorting Algorithm | n=100 | n=200 | n=400 | n=800 | n=1000 | n=2000")
for algo in average_time[sizes_to_test[0]].keys():
    results = [f"{average_time[size][algo]:.2f}" for size in sizes_to_test]
    print(f"{algo:<18} | {' | '.join(results)}")
