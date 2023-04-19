import unittest

def peak_mountain_array(arr):
    """Peak Mountain Array"""
    left, right = 0, len(arr)-1
    boundary_index = -1

    while left <= right:
        mid = (left + right) // 2
        if mid == len(arr) - 1 or arr[mid] > arr[mid+1]:
            boundary_index = mid
            right = mid - 1
        else:
            left = mid + 1

    return boundary_index


class TestPeakMountain(unittest.TestCase):
    """
    Test Peak Mountain
    """
    def test_in_the_middle(self):
        """
        Test In The Middle
        """
        # arrange
        arr = [0, 1, 2, 3, 2, 1, 0]
        expecting = 3

        # action
        result = peak_mountain_array(arr)

        # assert
        assert result == expecting, f"expecting {expecting}, got {result}"

    def test_at_last_position(self):
        """
        Test at Last Position
        """
        # arrange
        arr = [0, 1, 2, 3]
        expecting = 3

        # action
        result = peak_mountain_array(arr)

        # assert
        assert result == expecting, f"expecting {expecting}, got {result}"


if __name__ == "__main__":
    unittest.main()
