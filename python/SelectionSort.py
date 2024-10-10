def selection_sort(arr: list) -> list:
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def select_sort_with_enumerate(arr: list) -> list:
    for i in range(len(arr)):
        min_idx = i
        for idx, num in enumerate(arr[i + 1:], start = i + 1):
            if num < arr[min_idx]:
                min_idx = idx
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

arr = [9, 13, 18, 20, 1, 6]
result = selection_sort(arr)
print(result)