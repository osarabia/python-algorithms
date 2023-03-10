import unittest


def findThreeLargestNumbers(array):
    # search for max
    for i in range(0, len(array)-1):
        # swapping to let maxNumber at the end
        if array[i] > array[i+1]:
            tmp = array[i]
            array[i] = array[i+1]
            array[i+1] = tmp

    for i in range(0, len(array) - 2):
        if array[i] > array[i+1]:
            tmp = array[i]
            array[i] = array[i+1]
            array[i+1] = tmp

    for i in range(0, len(array) - 3):
        if array[i] > array[i+1]:
            tmp = array[i]
            array[i] = array[i+1]
            array[i+1] = tmp

    return [array[-3], array[-2], array[-1]]


class TestFindThreeLargest(unittest.TestCase):
    def test_no_duplicates(self):
        # arrange
        array = [5, 1, 20, 60, 12]
        expected = [12, 20, 60]

        # action
        result = findThreeLargestNumbers(array)

        # assert
        assert result == expected, "should be equals to {}".format(expected)

    def test_duplicates(self):
        # arrange
        array = [5, 1, 20, 60, 12, 60, 60]
        expected = [60, 60, 60]

        # action
        result = findThreeLargestNumbers(array)

        # assert
        assert result == expected, "should be equals to {}".format(expected)

    def test_negatives(self):
        # arrange
        array = [-20, -1, 0, -2, -5, -6, -222]
        expected = [-2, -1, 0]
        # action
        result = findThreeLargestNumbers(array)

        # assert
        assert result == expected, "should be equals to {}".format(expected)


if __name__ == "__main__":
    unittest.main()
