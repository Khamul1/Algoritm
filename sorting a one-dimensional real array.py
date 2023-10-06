import random

def merge_sort_asc(arr):
    if len(arr) < 2:
        return arr
    
    mid = len(arr) // 2

    left = merge_sort_asc(arr[:mid])
    right = merge_sort_asc(arr[mid:])

    merged = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged += left[i:]
    merged += right[j:]

    return merged

arr = [random.uniform(0, 50) for _ in range(10)]
print(f"Исходный массив: {arr}")

sorted_arr = merge_sort_asc(arr)
print(f"Отсортированный массив: {sorted_arr}")
