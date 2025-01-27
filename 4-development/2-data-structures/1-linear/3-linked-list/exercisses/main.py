from linked_list import LinkedList

def main():
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(4)
    linked_list.append(5)
    linked_list.print()

    linked_list.prepend(0)
    linked_list.print()

    linked_list.remove(3)
    linked_list.print()

    linked_list.remove(0)
    linked_list.print()

    linked_list.remove(5)
    linked_list.print()

if __name__ == '__main__':
    main()
