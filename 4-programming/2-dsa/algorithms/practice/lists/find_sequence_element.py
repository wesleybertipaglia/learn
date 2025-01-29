# Problem: 

def solution(arr):
    last = arr[-1]
    total_sum = last * (last + 1) // 2
    return total_sum - sum(arr)

def main():
    print(solution([1, 2, 3, 5]))

if __name__ == '__main__':
    main()
