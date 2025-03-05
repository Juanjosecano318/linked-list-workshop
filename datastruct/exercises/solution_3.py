from datastruct.classes.lists import LinkedList


def sort_list_by_insertion(linked_list: LinkedList[int]) -> LinkedList[int]:
    if not linked_list.head or not linked_list.head.next:
        return linked_list

    dummy = LinkedList()
    current = linked_list.head  # Nodo actual que estamos insertando

    while current:
        prev = dummy.head  # Apuntador previo para encontrar la posición correcta
        next_node = current.next  # Guardamos el siguiente nodo

        # Crear un nuevo nodo para insertar en la lista ordenada
        new_node = LinkedList.append(current.data)

        # Si la lista ordenada está vacía o el primer elemento es mayor
        if not dummy.head or dummy.head.data >= new_node.val:
            new_node.next = dummy.head
            dummy.head = new_node
        else:
            # Encontrar la posición correcta en la lista ordenada
            while prev.next and prev.next.data < new_node.val:
                prev = prev.next

            # Insertar el nodo en la posición correcta
            new_node.next = prev.next
            prev.next = new_node

        # Avanzar al siguiente nodo
        current = next_node

    linked_list.head = dummy.head  # Actualizar la cabeza de la lista original
    return linked_list


