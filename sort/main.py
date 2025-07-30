import timeit

import numpy as np

def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1 ):
            if arr[j] > arr[j + 1]:
                temp = arr[j+1]
                arr[j + 1] = arr[j]
                arr[j] = temp
    return arr

def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        id_min = i
        for j in range(i+1, n):
            if arr[id_min] > arr[j]:
                id_min = j
        temp = arr[id_min]
        arr[id_min] = arr[i]
        arr[i] = temp

    return arr

def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        temp = arr[i]

        j = i-1

        while j >= 0 and temp < arr[j]:
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = temp

    return arr

def shell_sort(arr):
    interval = len(arr) // 2

    while interval > 0:
        for i in range (interval, len(arr)):
            temp = arr[i]
            j=i
            while j >= interval and arr[j - interval] > temp:
                arr[j] = arr[j - interval]
                j -= interval
            arr[j] = temp

        interval //= 2

    return arr

print(bubble_sort(np.array([15, 34, 8, 3, 9])))
print(bubble_sort(np.array([34, 15, 10, 9, 6, 4, 3, 1, 0])))

print(selection_sort(np.array([15, 34, 8, 3, 9])))
print(selection_sort(np.array([34, 15, 10, 9, 6, 4, 3, 1, 0])))

print(insertion_sort(np.array([15, 34, 8, 3, 9])))
print(insertion_sort(np.array([34, 15, 10, 9, 6, 4, 3, 1, 0])))

print(shell_sort(np.array([15, 34, 8, 3, 9])))
print(shell_sort(np.array([34, 15, 10, 9, 6, 4, 3, 1, 0])))

# Medir o tempo de execução com timeit
execution_bubble = timeit.timeit(
    stmt='bubble_sort(np.array([15, 34, 8, 3, 9]))',
    globals=globals(),
    number=1000
)

execution_selection = timeit.timeit(
    stmt='selection_sort(np.array([15, 34, 8, 3, 9]))',
    globals=globals(),
    number=1000
)

execution_insertion = timeit.timeit(
    stmt='insertion_sort(np.array([15, 34, 8, 3, 9]))',
    globals=globals(),
    number=1000
)

print(f"Tempo de execução médio para bubble para 1000 execuções: {execution_bubble:.6f} segundos")
print(f"Tempo de execução médio para selection para 1000 execuções: {execution_selection:.6f} segundos")
print(f"Tempo de execução médio para insertion para 1000 execuções: {execution_insertion:.6f} segundos")
