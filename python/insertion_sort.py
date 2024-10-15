def insertion_sort(arr: list) -> list:
    arr_len = len(arr)
    for i in range(1, arr_len):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
        

arr = [4, 1, 6, 3, 28, 2, 9]    
print("========정렬 전========")    
print(arr)

insertion_sort(arr) 

print("========정렬 후========")
print(arr)