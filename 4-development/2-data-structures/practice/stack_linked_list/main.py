from stack_linked import Stack

def main():
    print(" STACK (LINKED LIST) ".center(40, "-"))

    stack = Stack()
    print("PUSH:", stack.push(10))
    print("PUSH:", stack.push(20))
    print("PUSH:", stack.push(30))
    print("PUSH:", stack.push(40))
    print("PUSH:", stack.push(50), "\n")

    print("POP:", stack.pop())
    print("PEEK:", stack.peek(), "\n")

    print("POP:", stack.pop())
    print("PEEK:", stack.peek(), "\n")

    print("POP:", stack.pop())
    print("PEEK:", stack.peek(), "\n")

    stack.print()

if __name__ == '__main__':
    main()
