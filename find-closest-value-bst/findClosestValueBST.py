import unittest


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def findClosestValueBST(tree, target):
    distance = abs(target - tree.value)
    value = tree.value

    currentNode = tree
    while currentNode is not None:
        diff = abs(target - currentNode.value)
        if diff < distance:
            distance = diff
            value = currentNode.value
        if target > currentNode.value:
            currentNode = currentNode.right
        else:
            currentNode = currentNode.left
    return value


class TestFindClosesValueBST(unittest.TestCase):
    def test_short_tree(self):
        # arrange
        root = BST(10)
        root.left = BST(9)
        root.right = BST(12)
        expected = 12
        # action
        value = findClosestValueBST(root, 13)

        # assert
        assert value == expected, "value should be {}".format(expected)

    def test_large_tree(self):
        # arrange
        root = BST(100)
        root.left = BST(1)
        root.right = BST(120)
        root.left.left = BST(0)
        root.left.right = BST(2)
        root.right.right = BST(125)
        root.right.left = BST(115)

        expected = 115
        # action
        value = findClosestValueBST(root, 113)

        # assert
        assert value == expected, "value should be {}".format(expected)


if __name__ == "__main__":
    unittest.main()
