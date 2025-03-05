from datastruct.classes.lists import LinkedList


def swap_nodes_in_pairs(linked_list: LinkedList[int]) -> LinkedList[int]:

    if not linked_list.head:
        return linked_list
    if not linked_list.head.next:
        return linked_list

    #Inicializamos
    head = linked_list.head
    second = head.next
    prev = None
    first = head

    while first and first.next:
        second = first.next  # Apuntamos al segundo nodo del par
        first.next = second.next  # Conectamos el primer nodo al siguiente nodo después del par
        second.next = first  # Intercambiamos el orden

        if prev:
            prev.next = second # Conectamos el nodo previo con el nuevo primer nodo del par

        prev = first
        first = first.next

    linked_list.head = second
    return linked_list










