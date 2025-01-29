# Problem: return the square root of a number

def solution(num):
    return num**(1/2)

def main():
    print(f"{float(solution(36)):.2}")
    print(f"{float(solution(49)):.2}")
    print(f"{float(solution(64)):.2}")

if __name__ == '__main__':
    main()
