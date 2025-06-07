import timeit
import random
import heapq

# --- Сортування вставками ---
def insertion_sort(arr):
    a = arr.copy()
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a

# --- Сортування злиттям ---
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# --- Вбудоване сортування Python (Timsort) ---
def timsort(arr):
    return sorted(arr)

# --- Функція для тестування часу ---
def test_sorts(sizes, repeats=3):
    print(f"{'Розмір':>8} | {'Insertion':>10} | {'Merge':>10} | {'Timsort':>10}")
    print("-"*45)
    for size in sizes:
        data = [random.randint(0, 100000) for _ in range(size)]
        
        insertion_time = timeit.timeit(lambda: insertion_sort(data), number=repeats) / repeats
        merge_time = timeit.timeit(lambda: merge_sort(data), number=repeats) / repeats
        timsort_time = timeit.timeit(lambda: timsort(data), number=repeats) / repeats
        
        print(f"{size:8} | {insertion_time:10.6f} | {merge_time:10.6f} | {timsort_time:10.6f}")

# --- Додаткове завдання: Об'єднання k відсортованих списків ---
def merge_k_lists(lists):
    merged = []
    heap = []
    
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst[0], i, 0))
    
    while heap:
        val, list_i, elem_i = heapq.heappop(heap)
        merged.append(val)
        if elem_i + 1 < len(lists[list_i]):
            heapq.heappush(heap, (lists[list_i][elem_i+1], list_i, elem_i+1))
    
    return merged

# --- Тестування коду ---
if __name__ == "__main__":
    sizes = [100, 1000, 5000, 10000]
    test_sorts(sizes)
    
    # Приклад роботи merge_k_lists
    lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    print("\nПриклад об'єднання k відсортованих списків:")
    print("Вхідні списки:", lists)
    print("Об'єднаний список:", merge_k_lists(lists))
    