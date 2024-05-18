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
    return None


numbers = [1,3,5,7,8,9,11,13,15,16,17,20,26,28,35,38,39,40]
print(binary_search(numbers, 20))