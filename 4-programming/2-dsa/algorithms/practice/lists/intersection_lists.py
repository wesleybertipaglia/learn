# Problem: 

def solution(arr1, arr2):
    result = set(arr1) & set(arr2)
    return list(result)

def main():
    print(solution([1,2,3,4,5], [2,3,4]))

if __name__ == '__main__':
    main()
