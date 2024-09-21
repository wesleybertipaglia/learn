# Problem: Verificar se uma string contendo os caracteres '(', ')', '{', '}', '[' e ']' é válida, ou seja, se os parênteses são bem formados.

def solution(s):
    parentheses = {')':'(', '}':'{', ']':'['}
    seen = []

    for char in s:
        if char in parentheses:
            if not seen or parentheses[char] != seen.pop(): # ()[]{}
                return False
        else:
            seen.append(char)
                
    return not seen

def main():
    print(solution("()[]{}"))

if __name__ == '__main__':
    main()
