def median_of_three_pivot(arr):
    if len(arr) <= 1:
        return 0, arr

    # Choose three elements: first, middle, and last
    first, middle, last = arr[0], arr[(len(arr)-1)//2], arr[-1]

    # Find the median element
    pivot = sorted([first, middle, last])[1]

    # Swap pivot with the first element
    pivot_index = arr.index(pivot)
    arr[pivot_index], arr[0] = arr[0], arr[pivot_index]

    # Initialize comparisons with the number of elements minus one
    comparisons = len(arr) - 1

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

    left_comparisons, left_sorted = median_of_three_pivot(low)
    right_comparisons, right_sorted = median_of_three_pivot(high)

    return comparisons + left_comparisons + right_comparisons, left_sorted + [pivot] + right_sorted

# Read data from the file
with open('input.txt', 'r') as file:
    input_array = [int(line) for line in file]

# Calculate the number of comparisons
total_comparisons_median_of_three, sorted_array_median_of_three = median_of_three_pivot(input_array)

# Print the result
print("Total number of comparisons using median-of-three pivot rule:", total_comparisons_median_of_three)
