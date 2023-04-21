import unittest

def is_monotonic_array(array):
    if len(array) <= 1:
        return True

    index = 1
    # choose direction
    if array[0] > array[-1]:
        while index <= len(array) - 1 and array[index-1] >= array[index]:
            index += 1
    else:
        while index <= len(array) - 1 and array[index-1] <= array[index]:
            index += 1
    #we should finish walking all elements of the array
    if index == len(array):
        return True
    return False


class TestIsMonotonicArray(unittest.TestCase):
    """
    Test Is Monotonic Array
    """

    def test_valid_case(self):
        """
        test valid case
        """
        # arrange
        arr = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
        expecting = True

        # action
        result = is_monotonic_array(arr)

        # assert
        assert result == expecting, f"expecting {expecting}, got {result}"

    def test_invalid(self):
        """
        test invalid case
        """
        # arrange
        arr = [-1, -5, -10, -1100, -900, -1101, -1102, -9001]
        expecting = False

        # action
        result = is_monotonic_array(arr)

        # assert
        assert result == expecting, f"expecting {expecting}, got {result}"


if __name__ == "__main__":
    unittest.main()