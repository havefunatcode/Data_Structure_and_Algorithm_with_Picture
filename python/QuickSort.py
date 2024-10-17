def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def quick_sort_in_place(arr):
    def sort(left, right):
        if left >= right:
            return
        
        mid = partition(left, right)
        sort(left, mid - 1)
        sort(mid, right)
        
    def partition(left, right):
        pivot = arr[(left + right) // 2]
        while left <= right:
            while arr[left] < pivot:
                left += 1
            while arr[right] > pivot:
                right -= 1
            if left <= right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
        return left
            
    return sort(0, len(arr) - 1)

sample_data = [38, 27, 43, 3, 9, 82, 10]
sorted_data1 = quick_sort(sample_data)
quick_sort_in_place(sample_data)
print(sorted_data1)
print(sample_data)