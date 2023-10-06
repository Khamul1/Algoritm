import random

def bubble_sort_dsc(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1],arr[j]
                swapped = True

        if not swapped:
            return arr
        return arr

arr = [random.randint(-100, 100) for _ in range(10)]
print(f"Исходный массив:{arr}")

sorted_arr = bubble_sort_dsc(arr)
print(f"Отсорированный массив: {sorted_arr}")


