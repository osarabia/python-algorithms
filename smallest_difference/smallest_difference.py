import unittest


def smallest_difference(array_one, array_two):
    """
    find the pair of values between two unsorted arrays whose differennce is
    closest to zero
    """
    array_one.sort()
    array_two.sort()

    min_pair_array = []
    min_pair_size = None

    for value in array_one:
        min_pair_array_iteration = [value, array_two[0]]
        min_pair_size_iteration = abs(value - array_two[0])

        # following loop to calculate min of each element on array_two
        for j in range(1, len(array_two)):
            diff = abs(value - array_two[j])
            if diff < min_pair_size_iteration:
                min_pair_array_iteration = [value, array_two[j]]
                min_pair_size_iteration = diff
            else:
                break
        if min_pair_size is None or min_pair_size_iteration < min_pair_size:
            min_pair_size = min_pair_size_iteration
            min_pair_array = min_pair_array_iteration
    return min_pair_array


class TestSmallestDifference(unittest.TestCase):
    """
    Test to Find Smallest Diffrence
    """
    def test_same_length(self):
        """
        Test arrays of same length
        """
        # arrange
        array_one = [-1, 5, 10, 20, 28, 3]
        array_two = [26, 134, 135, 15, 17]
        expected = [28, 26]

        # action
        result = smallest_difference(array_one, array_two)

        # assert
        assert result == expected, f"expecting {expected}, got {result}"


if __name__ == "__main__":
    unittest.main()
