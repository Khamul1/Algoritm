import random

arr = [random.randint(1, 100) for _ in range(10)]
print("Исходный список:", arr)

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        is_sorted = True  # Инициализация булевской переменной
        right_border = n - i - 1
        left_border = i # перемнная left_border иницализируется значем i, которое указвывает на крайний левый элемент неотсортированной части списка
        for j in range(right_border):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                is_sorted = False # перевод флага в False, если выполнена перестановка
                right_border = j # обновление правой границы
        if is_sorted:
            break # прерывание цикла, если булеевская переменная не поменялся
    return arr

arr = bubble_sort(arr)
print("Отсортированный список:", arr)