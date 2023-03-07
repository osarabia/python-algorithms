import unittest

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def reverse(head):
    previous, current = None, head
    while current is not None:
        nextNode = current.next
        #invert direction
        current.next = previous
        previous = current
        current = nextNode
    return previous

class TestReverseLinkedList(unittest.TestCase):
    def test_reverse(self):
        #arrange
        head = LinkedList(5)
        head.next = LinkedList(4)
        head.next.next = LinkedList(3)

        #action
        tailAsHead = reverse(head)

        first = tailAsHead.value
        second = tailAsHead.next.value
        third = tailAsHead.next.next.value
        assert first == 3,"expecting {}, got {}".format(3, first)
        assert second == 4, "expecting {}, got {}".format(4, second)
        assert third == 5, "expecting {}, got {}".format(5, third)

if __name__ == "__main__":
    unittest.main()
