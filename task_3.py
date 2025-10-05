import random
import timeit

# ---------------- Сортування вставками ----------------
def insertion_sort(arr): 
    arr = arr[:] 
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
# ---------------- Сортування злиттям ----------------
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)
def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
# ---------------- Тестування ----------------
def benchmark():
    sizes = [1000, 5000, 10000, 20000] 
    results = []
    for size in sizes:
        data = [random.randint(0, 100000) for _ in range(size)]
        t_insertion = timeit.timeit(lambda: insertion_sort(data), number=1)
        t_merge = timeit.timeit(lambda: merge_sort(data), number=1)
        t_timsort = timeit.timeit(lambda: sorted(data), number=1)
        results.append((size, t_insertion, t_merge, t_timsort))
    return results
# ---------------- Головна функція ----------------
if __name__ == "__main__":
    results = benchmark()
    print("Розмір | Вставками | Злиттям | Timsort (sorted)")
    print("-" * 50)
    for size, t1, t2, t3 in results:
        print(f"{size:6} | {t1:.6f} c | {t2:.6f} c | {t3:.6f} c")