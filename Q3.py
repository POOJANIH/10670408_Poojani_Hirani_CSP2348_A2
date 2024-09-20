import random
import time

# Sorting Algorithms with Comparison and Timing

def selection_sort(arr):
    comparisons = 0
    swaps = 0
    n = len(arr)
    start = time.time()
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            comparisons += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        swaps += 1
    end = time.time()
    return arr, comparisons, swaps, (end - start) * 1000

def insertion_sort(arr):
    comparisons = 0
    swaps = 0
    n = len(arr)
    start = time.time()
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            comparisons += 1
            arr[j + 1] = arr[j]
            j -= 1
        comparisons += 1
        arr[j + 1] = key
    end = time.time()
    return arr, comparisons, swaps, (end - start) * 1000

def merge_sort(arr):
    comparisons = 0
    swaps = 0
    def merge(left, right):
        nonlocal comparisons
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            comparisons += 1
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def divide(arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = divide(arr[:mid])
        right = divide(arr[mid:])
        return merge(left, right)

    start = time.time()
    sorted_arr = divide(arr)
    end = time.time()
    return sorted_arr, comparisons, swaps, (end - start) * 1000

def quick_sort(arr):
    comparisons = 0
    swaps = 0
    def partition(low, high):
        nonlocal comparisons, swaps
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            comparisons += 1
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                swaps += 1
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        swaps += 1
        return i + 1

    def divide(low, high):
        if low < high:
            pi = partition(low, high)
            divide(low, pi - 1)
            divide(pi + 1, high)

    start = time.time()
    divide(0, len(arr) - 1)
    end = time.time()
    return arr, comparisons, swaps, (end - start) * 1000

def heap_sort(arr):
    comparisons = 0
    swaps = 0
    def heapify(n, i):
        nonlocal comparisons, swaps
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n:
            comparisons += 1
            if arr[l] > arr[largest]:
                largest = l
        if r < n:
            comparisons += 1
            if arr[r] > arr[largest]:
                largest = r
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            swaps += 1
            heapify(n, largest)

    n = len(arr)
    start = time.time()
    for i in range(n // 2 - 1, -1, -1):
        heapify(n, i)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        swaps += 1
        heapify(i, 0)
    end = time.time()
    return arr, comparisons, swaps, (end - start) * 1000

def bubble_sort(arr):
    comparisons = 0
    swaps = 0
    n = len(arr)
    start = time.time()
    for i in range(n):
        for j in range(0, n - i - 1):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
    end = time.time()
    return arr, comparisons, swaps, (end - start) * 1000

def obs1_bubble_sort(arr):
    comparisons = 0
    swaps = 0
    n = len(arr)
    start = time.time()
    for i in range(n):
        for j in range(0, n - i - 1):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
    end = time.time()
    return arr, comparisons, swaps, (end - start) * 1000

def obs2_bubble_sort(arr):
    comparisons = 0
    swaps = 0
    n = len(arr)
    start = time.time()
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
                swapped = True
        if not swapped:
            break
    end = time.time()
    return arr, comparisons, swaps, (end - start) * 1000

def obs3_bubble_sort(arr):
    comparisons = 0
    swaps = 0
    n = len(arr)
    start = time.time()
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
                swapped = True
        if not swapped:
            break
    end = time.time()
    return arr, comparisons, swaps, (end - start) * 1000

def sink_down_sort(arr):
    comparisons = 0
    swaps = 0
    n = len(arr)
    start = time.time()
    for i in range(n):
        for j in range(n - 1, i, -1):
            comparisons += 1
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                swaps += 1
    end = time.time()
    return arr, comparisons, swaps, (end - start) * 1000

def bi_directional_bubble_sort(arr):
    comparisons = 0
    swaps = 0
    n = len(arr)
    start = time.time()
    left = 0
    right = n - 1
    while left < right:
        for i in range(left, right):
            comparisons += 1
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swaps += 1
        right -= 1
        for i in range(right, left, -1):
            comparisons += 1
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                swaps += 1
        left += 1
    end = time.time()
    return arr, comparisons, swaps, (end - start) * 1000

# Main Menu System

def main_menu():
    while True:
        print("\nMain Menu:")
        print("1. Test an individual sorting algorithm")
        print("2. Test multiple sorting algorithms")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            test_individual_algorithm()
        elif choice == '2':
            test_multiple_algorithms()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

def test_individual_algorithm():
    print("\nChoose sorting algorithm:")
    print("1. Selection Sort")
    print("2. Insertion Sort")
    print("3. Merge Sort")
    print("4. Quick Sort")
    print("5. Heap Sort")
    print("6. Bubble Sort")
    print("7. Obs1 Bubble Sort")
    print("8. Obs2 Bubble Sort")
    print("9. Obs3 Bubble Sort")
    print("A. Sink-Down Sort")
    print("B. Bi-Directional Bubble Sort")

    algo_choice = input("Enter your choice: ")
    size = int(input("Enter size of the array (n>0): "))
    arr = [random.randint(0, 1000) for _ in range(size)]

    algorithms = {
        '1': selection_sort,
        '2': insertion_sort,
        '3': merge_sort,
        '4': quick_sort,
        '5': heap_sort,
        '6': bubble_sort,
        '7': obs1_bubble_sort,
        '8': obs2_bubble_sort,
        '9': obs3_bubble_sort,
        'A': sink_down_sort,
        'B': bi_directional_bubble_sort
    }

    if algo_choice in algorithms:
        sorted_arr, comparisons, swaps, runtime = algorithms[algo_choice](arr.copy())
        print(f"\nResults for {algo_choice}:")
        print(f"Array Size: {size}, Comparisons: {comparisons}, Runtime: {runtime:.2f} ms")
    else:
        print("Invalid choice. Returning to main menu.")

def test_multiple_algorithms():
    size = int(input("Enter size of the array (n>0): "))
    arr = [random.randint(0, 1000) for _ in range(size)]

    print("\nSorting algorithm name | Array size | Num. of Comparisons | Run time (in ms)")
    print("-" * 70)

    algorithms = {
        'Selection Sort': selection_sort,
        'Insertion Sort': insertion_sort,
        'Merge Sort': merge_sort,
        'Quick Sort': quick_sort,
        'Heap Sort': heap_sort,
        'Bubble Sort': bubble_sort,
        'Obs1 Bubble Sort': obs1_bubble_sort,
        'Obs2 Bubble Sort': obs2_bubble_sort,
        'Obs3 Bubble Sort': obs3_bubble_sort,
        'Sink-Down Sort': sink_down_sort,
        'Bi-Directional Bubble Sort': bi_directional_bubble_sort
    }

    for name, algorithm in algorithms.items():
        sorted_arr, comparisons, swaps, runtime = algorithm(arr.copy())
        print(f"{name:<25} | {size:<10} | {comparisons:<20} | {runtime:.2f}")

if __name__ == "__main__":
    main_menu()
