from datastruct.classes.lists import LinkedList


def add_two_numbers(l1: LinkedList[int], l2: LinkedList[int]) -> LinkedList[int]:
    result = LinkedList[int]()
    carry = 0

    node1, node2 = l1.head, l2.head

    while node1 or node2 or carry:

        val1 = node1.data if node1 else 0
        val2 = node2.data if node2 else 0

        total = val1 + val2 + carry
        carry = total // 10
        result.append(total % 10)

        if node1:
            node1 = node1.next
        if node2:
            node2 = node2.next

    if carry:
        result.append(carry)

    return result














