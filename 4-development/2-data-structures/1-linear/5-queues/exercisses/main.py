from queue_list import Queue

def main():
    print(" QUEUE (LIST) ".center(40, "-"))

    queue = Queue()
    print("ENQUEUE:", queue.enqueue(10))
    print("ENQUEUE:", queue.enqueue(20))
    print("ENQUEUE:", queue.enqueue(30))
    print("ENQUEUE:", queue.enqueue(40))
    print("ENQUEUE:", queue.enqueue(50), "\n")

    print("DEQUEUE:", queue.dequeue())
    print("PEEK:", queue.peek(), "\n")

    print("DEQUEUE:", queue.dequeue())
    print("PEEK:", queue.peek(), "\n")

    print("DEQUEUE:", queue.dequeue())
    print("PEEK:", queue.peek(), "\n")

    queue.print()

if __name__ == '__main__':
    main()
