import unittest


class ListNode:
    """
    List Node Class container
    """
    def __init__(self, value=0,next=None):
        self.value = value
        self.next = next


def linked_list_cycle_hashset(head):
    """
    Detect Linked List Cycle Hash Set Approach
    """
    if head is None:
        return False
    seen = set()

    seen.add(head)

    while head:
        head = head.next
        if head and head in seen:
            return True
        seen.add(head)

    return False


def linked_list_cycle(head):
    """
    slow_pointer, fast pointer approach
    """
    if head is None:
        return False
    fast_pointer = head
    while head.next and fast_pointer.next.next:
        head = head.next
        fast_pointer = fast_pointer.next.next
        if head == fast_pointer:
            return True
    return False


class TestLinkedListCycle(unittest.TestCase):
    """
    Test to Detect Linked List Cycle
    """

    def test_cycle_existence(self):
        """
        Test One Linked List
        """
        # arrange
        head = ListNode(3)
        head.next = ListNode(2)
        head.next.next = ListNode(0)
        head.next.next.next = ListNode(-4)
        head.next.next.next.next = head.next

        # action
        result = linked_list_cycle_hashset(head)

        # assert
        assert result, f"expecting {True}, got {result}"
    
    def test_cycle_existence_floyd_algo(self):
        """
        Test One Linked List
        """
        # arrange
        head = ListNode(3)
        head.next = ListNode(2)
        head.next.next = ListNode(0)
        head.next.next.next = ListNode(-4)
        head.next.next.next.next = head.next

        # action
        result = linked_list_cycle(head)

        # assert
        assert result, f"expecting {True}, got {result}"

    def test_no_cycle(self):
        """
        Test no cycle at all
        """
        # arrange
        head = ListNode(1, ListNode(2))

        # action
        result = linked_list_cycle(head)

        # assert
        assert result is False, "expecting {False}, got {result}"


if __name__ == "__main__":
    unittest.main()
