def bubble_sort(arr: list) -> list:
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

arr = [9, 13, 18, 20, 1, 6]
result = bubble_sort(arr)
print(result) 