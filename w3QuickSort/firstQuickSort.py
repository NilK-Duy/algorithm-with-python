def quicksort_comparison_count(arr):
    # Base case: if the array has one element or is empty, no comparisons needed
    if len(arr) <= 1:
        return 0, arr

    # Initialize comparisons with the number of elements minus one
    comparisons = len(arr) - 1
    # Choose the first element as the pivot
    pivot = arr[0]

    # Initialize the index to track the position to swap
    swap_index = 1

    # Iterate through the array starting from the second element
    for i in range(1, len(arr)):
        if arr[i] < pivot:
            # Swap current element with the element at swap_index
            arr[i], arr[swap_index] = arr[swap_index], arr[i]
            # Move the swap_index to the next position
            swap_index += 1

    # Swap the pivot with the last element in the lower partition
    arr[0], arr[swap_index - 1] = arr[swap_index - 1], arr[0]

    # Partition the array into low and high based on the swap_index
    low = arr[:swap_index - 1]
    high = arr[swap_index:]

    # Recursively perform QuickSort on the low and high partitions
    left_comparisons, left_sorted = quicksort_comparison_count(low)
    right_comparisons, right_sorted = quicksort_comparison_count(high)

    # Combine the results and the pivot to get the fully sorted array
    return comparisons + left_comparisons + right_comparisons, left_sorted + [pivot] + right_sorted

# Read data from the file
with open('input.txt', 'r') as file:
    input_array = [int(line) for line in file]

# Calculate the total number of comparisons and obtain the sorted array
total_comparisons, sorted_array = quicksort_comparison_count(input_array)

# Print the result
print("Total number of comparisons:", total_comparisons)
