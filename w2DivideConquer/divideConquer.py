def count_inversions(arr):
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2
    left, inv_left = count_inversions(arr[:mid])
    right, inv_right = count_inversions(arr[mid:])
    merged, split_inv = merge_and_count(left, right)

    total_inv = inv_left + inv_right + split_inv

    return merged, total_inv

def merge_and_count(left, right):
    merged = []
    i, j, split_inv = 0, 0, 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            split_inv += len(left) - i
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged, split_inv

# Read the input file
with open("test/testPython\input.txt", "r") as file:
    array = [int(line.strip()) for line in file]

# Count inversions using the divide-and-conquer algorithm
sorted_array, inversion_count = count_inversions(array)

# Print the result (numeric answer) for the given input file
print(inversion_count)