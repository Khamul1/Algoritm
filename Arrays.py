import random

arr = [random.randint(-100, 100) for _ in range(10)]
print(f"Исходный массив: {arr}")

min_index = arr.index(min(arr))
max_index = arr.index(max(arr))

arr[min_index], arr[max_index] = arr[max_index], arr[min_index]

print(f"Массив с поменяными местами минимальным и максимальным элементами: {arr}")  