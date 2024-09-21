# Problem: Dado um array de inteiros e um valor-alvo, encontrar dois números no array que somem o valor-alvo

def solution(arr, target) -> int:
    seen = set()

    for i, value in enumerate(arr):
        diff = target - value

        if diff in seen:
            return value, diff

        seen.add(value)
    return -1

def main():
    print(solution([1,2,3,4,5,7], 9))
    print(solution([1,2,3,5], 9))

if __name__ == '__main__':
    main()
