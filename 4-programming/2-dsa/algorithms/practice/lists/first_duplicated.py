# Problem: 

def solution(arr):
    seen = set()
    for num in arr:
        if num in seen:
            return num
        seen.add(num)
    return -1

def main():
    print(solution([1,2,3,4,5,6,5]))

if __name__ == '__main__':
    main()
