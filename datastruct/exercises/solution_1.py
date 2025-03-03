from datastruct.classes.lists import LinkedList


def add_two_numbers(l1: LinkedList[int], l2: LinkedList[int]) -> LinkedList[int]:
    # Implement solution here
    dummy_head = LinkedList(0)
    current = dummy_head
    carry = 0


