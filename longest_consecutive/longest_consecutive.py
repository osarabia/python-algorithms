import unittest


def longest_consecutives(array):
    """
        Unsorted array of integers, return the kength of longest consecutive sequence
    """
    max_sequence_size = 1
    nums = set()
    for number in array:
        nums.add(number)

    for number in array:
        left = number - 1
        if left not in nums:
            # we are at the sequence start number
            # let's go to right
            sequence_size = 1
            right = number + 1
            while right in nums:
                sequence_size += 1
                right = right + 1
            max_sequence_size = max(max_sequence_size, sequence_size)
    return max_sequence_size


class TestLongestSequence(unittest.TestCase):
    """
    Testing Longest Sequence
    """
    def test_start_at_tail(self):
        """
        Test start of sequence at the end of array
        """
        # arrange
        array = [100, 200, 201, 5, 2, 3, 4, 1]
        expected = 5

        # action
        result = longest_consecutives(array)

        # assert
        assert result == expected, f"expecting {expected}, got {result}"

    def test_at_start_postion(self):
        """
        Test start of sequence at first index
        """
        # arrange
        array = [20, 200, 500, 501, 21, 25, 22, 24, 23]
        expected = 6
        # action
        result = longest_consecutives(array)

        # assert
        assert result == expected, f"expecting {expected}, got {result}"


if __name__ == "__main__":
    unittest.main()
