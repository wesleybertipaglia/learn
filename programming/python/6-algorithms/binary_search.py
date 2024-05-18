def binary_search(items, target):
    start = 0
    end = len(items) - 1

    while start <= end:
        mid = (start + end) // 2
        
        if target == items[mid]:
            return mid
        elif target < items[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return -1