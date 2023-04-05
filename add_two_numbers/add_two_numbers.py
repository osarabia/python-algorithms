import unittest


class Node:
    """
    Node Class
    """

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def add_two_numbers(l_1, l_2):
    """
    Add Two Numbers as Linked List
    """
    carry = 0
    dummy_node = Node(0)
    node = dummy_node

    while l_1 and l_2:
        number_1 = l_1.val
        number_2 = l_2.val

        total = number_1 + number_2 + carry
        carry = total // 10
        number = total % 10
        node.next = Node(number)

        l_1 = l_1.next
        l_2 = l_2.next
        node = node.next

    while l_1:
        number_1 = l_1.val
        total = number_1 + carry
        carry = total // 10
        number = total % 10
        node.next = Node(number)
        l_1 = l_1.next
        node = node.next

    while l_2:
        number_2 = l_2.val
        total = number_2 + carry
        carry = total // 10
        number = total % 10
        node.next = Node(number)
        l_2 = l_2.next
        node = node.next
    
    if carry > 0:
        node.next = Node(carry)
    
    return dummy_node.next

class TestAddTwoNumbers(unittest.TestCase):

    def test_one(self):
        """
        Fist Test Case
        """
        # arrange
        l_1 = Node(2)
        l_1.next = Node(4)
        l_1.next.next = Node(3)

        l_2 = Node(5)
        l_2.next = Node(6)
        l_2.next.next = Node(4)

        # action
        result = add_two_numbers(l_1, l_2)

        # assert
        next_next_val = result.next.next.val
        assert result.val == 7, f"expecting 7 got {result.val}"
        assert result.next.val == 0, f"expecting 0 got {result.next.val}"
        assert next_next_val == 8, f"expeting 8 got {next_next_val}"


if __name__ == "__main__":
    unittest.main()
