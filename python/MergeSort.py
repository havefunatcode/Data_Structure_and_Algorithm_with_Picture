def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    result = []
    left_idx = right_idx = 0
    
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1
    
    result += left[left_idx:]
    result += right[right_idx:]
    return result

def merge_sort_in_place(arr):
    def sort(left, right):
        if right - left <= 1:
            return 
        
        mid = (left + right) // 2
        sort(left, mid)
        sort(mid, right)
        merge(left, mid, right)
        
    def merge(left, mid, right):
        temp = []
        left_idx, right_idx = left, mid
        
        while left_idx < mid and right_idx < right:
            if arr[left_idx] < arr[right_idx]:
                temp.append(arr[left_idx])
                left_idx += 1
            else:
                temp.append(arr[right_idx])
                right_idx += 1
        
        while left_idx < mid:
            temp.append(arr[left_idx])
            left_idx += 1
        while right_idx < right:
            temp.append(arr[right_idx])
            right_idx += 1
        
        for i in range(left, right):
            arr[i] = temp[i - left]
    return sort(0, len(arr))

sample_data = [38, 27, 43, 3, 9, 82, 10]
sorted_data1 = merge_sort(sample_data)
merge_sort_in_place(sample_data)
print(sorted_data1)
print(sample_data)