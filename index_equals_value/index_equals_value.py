import unittest


def index_equals_value(array):
    """
    min index where value and index are equals
    """
    min_value = -1
    low, high = 0, len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        if mid == array[mid]:
            min_value = mid
            high = mid - 1
        else:
            if array[mid] > mid:
                low = mid + 1
            else:
                high = mid - 1
    return min_value


class TestIndexEqualsValue(unittest.TestCase):
    """
        Test For Index Equals
    """
    def test_negatives(self):
        """
        Test Negatives Numbers
        """
        # arrange
        array = [-5, -3, 0, 3, 4, 5, 9]
        expected = 3

        # action
        result = index_equals_value(array)

        # assert
        assert result == expected, f"expecting {expected}, got {result}"

    def test_positives(self):
        """
        Test Positive Numbers
        """
        # arrange
        array = [0, 1, 2, 3, 4, 5]
        expected = 0

        # action
        result = index_equals_value(array)
        
        # assert
        assert result == expected, f"expecting {expected}, got {result}"

    def test_last_element(self):
        """
        Test last index
        """
        # arrange
        array = [2, 3, 4, 5, 5, 5]
        expected = 5

        # action
        result = index_equals_value(array)

        # assert
        assert result == expected, f"expecting {expected}, got {result}"


if __name__ == "__main__":
    unittest.main()