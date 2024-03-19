import json
import timeit
from random import shuffle
import matplotlib.pyplot as plt

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

test_sizes = [i * 10000 for i in range(1, 11)]

merge_sort_times = {}
insertion_sort_times = {}
timsort_times = {}

for size in test_sizes:
    with open('data.json', 'r') as file:
        array = json.load(file)
    
    array = array[:size]    
    shuffle(array)
    
    merge_sort_time = timeit.timeit('merge_sort(array.copy())', globals=globals(), number=1)
    merge_sort_times[size] = merge_sort_time
    print(f'Merge Sort: {size} elements - {merge_sort_time} seconds')
    
    insertion_sort_time = timeit.timeit('insertion_sort(array.copy())', globals=globals(), number=1)
    insertion_sort_times[size] = insertion_sort_time
    print(f'Insertion Sort: {size} elements - {insertion_sort_time} seconds')
    
    timsort_time = timeit.timeit('sorted(array.copy())', globals=globals(), number=1)
    timsort_times[size] = timsort_time
    print(f'Timsort: {size} elements - {timsort_time} seconds')

plt.figure(figsize=(10, 5))

plt.plot(list(merge_sort_times.keys()), list(merge_sort_times.values()), label='Merge Sort', marker='o')
plt.plot(list(insertion_sort_times.keys()), list(insertion_sort_times.values()), label='Insertion Sort', marker='o')
plt.plot(list(timsort_times.keys()), list(timsort_times.values()), label='Timsort', marker='o')

plt.xlabel('Number of elements')
plt.ylabel('Time (seconds)')
plt.title('Sorting Algorithm Performance')
plt.legend()

plt.grid(True)
plt.savefig('./plot.png')

