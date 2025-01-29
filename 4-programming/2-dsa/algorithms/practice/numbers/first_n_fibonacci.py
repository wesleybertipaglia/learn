# Problem: return the n first fibonacci numbers

def solution(num):
    sequencia = []
    a, b = 0, 1
    for _ in range(num):
        sequencia.append(a)
        a, b = b, a + b
    return sequencia

def main():
    print(solution(10))
    print(solution(21))
    print(solution(19))

if __name__ == '__main__':
    main()
