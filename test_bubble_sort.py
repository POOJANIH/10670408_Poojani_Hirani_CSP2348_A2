import random
import time

# Import sorting functions from respective files
from Obs1_bubble_sort import obs1_bubble_sort
from Obs2_bubble_sort import obs2_bubble_sort
from Obs3_bubble_sort import obs3_bubble_sort

def generate_random_array(size):
    return [random.randint(1, 1000) for _ in range(size)]

def test_sorting_algorithm(sort_function, array):
    start_time = time.time()
    sorted_array = sort_function(array)
    end_time = time.time()
    elapsed_time = (end_time - start_time) * 1000  # Convert to milliseconds
    return sorted_array, elapsed_time

def main():
    array_size = 20  # Test with an array of 20 elements
    original_array = generate_random_array(array_size)

    print(f"Original array: {original_array}")

    # Test Obs1-BubbleSort
    arr = original_array.copy()
    sorted_array, time_taken = test_sorting_algorithm(obs1_bubble_sort, arr)
    print(f"Obs1-BubbleSort - Sorted array: {sorted_array}")
    print(f"Obs1-BubbleSort - Time taken: {time_taken:.4f} ms")

    # Test Obs2-BubbleSort
    arr = original_array.copy()
    sorted_array, time_taken = test_sorting_algorithm(obs2_bubble_sort, arr)
    print(f"Obs2-BubbleSort - Sorted array: {sorted_array}")
    print(f"Obs2-BubbleSort - Time taken: {time_taken:.4f} ms")

    # Test Obs3-BubbleSort
    arr = original_array.copy()
    sorted_array, time_taken = test_sorting_algorithm(obs3_bubble_sort, arr)
    print(f"Obs3-BubbleSort - Sorted array: {sorted_array}")
    print(f"Obs3-BubbleSort - Time taken: {time_taken:.4f} ms")

if __name__ == "__main__":
    main()
