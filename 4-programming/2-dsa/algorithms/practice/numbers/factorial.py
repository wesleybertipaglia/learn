# Problem: return the factorial of a number

def solution(num):
    if num == 0 or num == 1:
        return 1
    
    return num * solution(num - 1)


def main():
    print(solution(1))
    print(solution(2))
    print(solution(3))
    print(solution(4))
    print(solution(5))
    print(solution(6))
    print(solution(7))
    print(solution(8))
    print(solution(9))

if __name__ == '__main__':
    main()
