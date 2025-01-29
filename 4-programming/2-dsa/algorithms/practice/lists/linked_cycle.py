# Problem: Determinar se uma lista encadeada possui um ciclo

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def solution(head):
    slow = head
    fast = head.next

    while slow != fast:
        if not fast:
            return False
        slow = slow.next
        fast = fast.next.next

    return True

def main():
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)

    node1.next = node2
    node2.next = node3
    node3.next = node1 # cycle

    print(solution(node1))

if __name__ == '__main__':
    main()
