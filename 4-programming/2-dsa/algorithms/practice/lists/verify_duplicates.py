# Problem: 

def solution(arr):
    return len(arr) != len(set(arr))

def main():
    print(solution([1,1,2,3,4,5,6,5,4,4]))

if __name__ == '__main__':
    main()
