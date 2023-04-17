import unittest

def find_first_element_greater_target(arr, target):
    """
    First Element greater than equals target
    """

    min_index = -1

    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (right + left) // 2
        if arr[mid] >= target:
            min_index = mid
            right = mid - 1
        else:
            left = mid + 1
    return min_index


class TestFindFirstElementGreaterEqualTarget(unittest.TestCase):
    """
    Test Find First Element Greater Than Equal Target
    """

    def test_find_in_duplicates(self):
        """
        Find First Index inside target
        """
        # arrange
        arr = [1, 2, 2, 2, 20, 21, 22]
        target = 3
        expecting = 4

        # action
        result = find_first_element_greater_target(arr, target)

        # assert
        assert result == expecting, f"expecting {expecting}, got {result}"

    def test_find_duplicates_targets(self):
        """
        Find inside duplicates targets
        """
        # arrange
        arr = [1, 2, 3, 3, 3, 4, 5]
        target = 3
        expecting = 2

        # action
        result = find_first_element_greater_target(arr, target)

        # assert
        assert result == expecting, f"expecting {expecting}, got {result}"


if __name__ == "__main__":
    unittest.main()