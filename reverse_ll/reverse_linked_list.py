
class Node:
    """
    Node Class for Linked List
    """
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def reverse_linked_list(head):
    """
    Reverse linked list
    """
    if head is None:
        return head

    previous = head
    current = head.next
    previous.next = None
    while current:
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node

    return previous


if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    result = reverse_linked_list(head)
    while result:
        print(result.value)
        result = result.next
