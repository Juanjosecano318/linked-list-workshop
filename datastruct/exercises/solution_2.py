from datastruct.classes.lists import LinkedList


def swap_nodes_in_pairs(linked_list: LinkedList[int]) -> LinkedList[int]:

    if not linked_list.head:
        return linked_list
    if not linked_list.head.next:
        return linked_list

    head = linked_list.head

    prev = None
    first = head
    second = head.next

    while first and first.next:
        second = first.next
        first.next = second.next
        if second:
            second.next = first
        if prev:
            pass













