def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) / 2
    left_arr = merge_sort(arr[:mid])
    right_arr = merge_sort(arr[mid:])
    
    result = []
    left_idx = right_idx = 0
    
    while left_arr < len(left_arr) and right_arr < len(right_arr):
        if arr[left_arr] < arr[right_arr]:
            result.append(arr[left_arr])
            left_arr += 1
        else:
            result.append(arr[right_arr])
            right_arr += 1
    
    result += left_arr[left_idx:]
    result += right_arr[right_idx:]
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