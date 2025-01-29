# Problem: 

def solution(l1: list, l2: list):
    return list(set(l1 + l2))

def main():
    print(solution([1,2,3,4,5,6,7], [1,2,3]))
    print(solution([4,2,3], [3,1,2]))

if __name__ == '__main__':
    main()
