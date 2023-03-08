import unittest

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return "{}:{}".format(id(self),self.value)


def findLoop(head):
    slow, fast = head.next, head.next.next

    #first we find a loop
    while slow != fast:
        slow = slow.next
        fast = fast.next.next
    #after this cycle we find the number of jumps inside the loop

    slow = head
    #slow and fast intersect at the beginning of the loop
    while slow != fast:
        slow = slow.next
        fast = fast.next.next
    return slow


class TestFindLoop(unittest.TestCase):
    def test_single_loop(self):
        #arrange
        head = LinkedList(5)
        head.next = head

        #action
        result = findLoop(head)

        #assert
        assert result == head, "expecting {}, got {}".format(head, result)

    def test_loop_of_3(self):
        #arrange
        head = LinkedList(5)
        head.next = LinkedList(4)
        head.next.next = LinkedList(3)
        head.next.next.next = head

        #action
        result = findLoop(head)

        #assert
        assert result == head, "expecting {}, got {}".format(head, result)

    def test_loop_of_4(self):
        #arrange
        head = LinkedList(5)
        head.next = LinkedList(4)
        head.next.next = LinkedList(3)
        head.next.next.next = LinkedList(2)

        head.next.next.next.next = head

        #action
        result = findLoop(head)

        #assert
        assert result == head, "expecting {}, got {}".format(head, result)


    def test_loop_of_5(self):
        #arrange
        head = LinkedList(5)
        head.next = LinkedList(4)
        head.next.next = LinkedList(3)
        head.next.next.next = LinkedList(2)

        head.next.next.next.next = head.next.next

        #action
        result = findLoop(head)

        #assert
        assert result == head.next.next, "expecting {}, got {}".format(head, result)




if __name__ == "__main__":
    unittest.main()
