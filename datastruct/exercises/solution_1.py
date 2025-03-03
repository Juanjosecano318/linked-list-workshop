from datastruct.classes.lists import LinkedList


def add_two_numbers(l1: LinkedList[int], l2: LinkedList[int]) -> LinkedList[int]:
    result = LinkedList[int]()
    carry = 0

    node1, node2 = l1.head, l2.head

    while l1 or l2 or carry:
        if l1:
            val1 = node1.data
        else:
            val1 = 0
        if l2:
            val2 = node2.data
        else:
            val2 = 0

        total = val1 + val2 + carry
        carry = total // 10
        result.append(total % 10)

        if node1:
            node1 = node1.next
        if node2:
            node2 = node2.next
    return result













