# Problem: return if a number is even or odd.

def solution(num):
    return "even" if num % 2 == 0 else "odd"

def main():
    print(solution(2)) # even
    print(solution(3)) # odd

if __name__ == '__main__':
    main()
