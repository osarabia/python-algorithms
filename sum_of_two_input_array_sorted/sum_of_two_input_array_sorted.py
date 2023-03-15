import unittest

def sum_of_II_input_array_sorted(numbers, target):
    """
    Sum of two numbers targets, return number one based index value
    """
    low, high = 0, len(numbers)-1

    while low <= high:
        result_sum = numbers[low] + numbers[high]
        if result_sum > target:
            high -= 1
        elif result_sum < target:
            low += 1
        else:
            return [low+1, high+1]


class TestSumIIInputArraySorted(unittest.TestCase):
    """
    Test Cases For Sum of II input array sorted
    """
    def test_example_1(self):
        """
        First Test
        """
        # arrange
        numbers = [2, 7, 11, 15]
        target = 9
        expected = [1, 2]

        # action
        result = sum_of_II_input_array_sorted(numbers, target)

        # assert
        assert result == expected, f"expecting {expected}, got {result}"

    def test_example_2(self):
        """
        Second Test
        """
        # arrange
        numbers = [2, 3, 4]
        target = 6
        expected = [1, 3]

        # action
        result = sum_of_II_input_array_sorted(numbers, target)

        # action
        result = sum_of_II_input_array_sorted(numbers, target)

        # assert
        assert result == expected, f"expecting {expected}, got {result}"

    def test_example_3(self):
        """
        Third Test
        """
        # arrange
        numbers = [1, 3, 4, 5, 7, 10, 11]
        target = 9
        expected = [3, 4]

        # action
        result = sum_of_II_input_array_sorted(numbers, target)

        # action
        result = sum_of_II_input_array_sorted(numbers, target)

        # assert
        assert result == expected, f"expecting {expected}, got {result}"


if __name__ == "__main__":
    unittest.main()
