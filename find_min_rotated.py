import unittest


def find_min_rotated(arr):
    left, right = 0, len(arr) -1
    boundary_index = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] <= arr[-1]:
            boundary_index = mid
            right = mid - 1
        else:
            left = mid + 1
    return boundary_index

class TestFindMinRotated(unittest.TestCase):
    """
    Test Cases Find Min Rotated
    """

    def test_middle(self):
        """
        Test at Middle
        """
        # arrange
        arr = [30, 40, 50, 10, 20]
        expecting = 3

        # action
        result = find_min_rotated(arr)

        # assert
        assert result == expecting, f"expecting {expecting}, got {result}"

    def test_end(self):
        """
        Test at Tail
        """
        # arrange
        arr = [3, 5, 7, 11, 13, 17, 19, 2]
        expecting = 7

        # action
        result = find_min_rotated(arr)

        # assert
        assert result == expecting, f"expecting {expecting}, got {result}"

if __name__ == "__main__":
    unittest.main()