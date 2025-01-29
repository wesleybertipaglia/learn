# Problem: 

def solution(arr: list, k: int):
    return arr[-k:] + arr[:-k] 

def main():
    print(solution([1,2,3,4,5,6], 3))

if __name__ == '__main__':
    main()
