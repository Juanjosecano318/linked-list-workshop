from datastruct.classes.lists import LinkedList


def swap_nodes_in_pairs(linked_list: LinkedList[int]) -> LinkedList[int]:

    lista = linked_list.head

    if lista is None:
        return linked_list
    if not lista.next:
        return linked_list






