import unittest


def search_2d_matrix(matrix, target):
    """
    Return True or False if target exists inside a matrix of m * n
    This matris is sorted
    """
    for m in matrix:
        left, right = 0, len(m) - 1
        while left <= right:
            index = (left + right) // 2
            value = m[index]
            if target == value:
                return True
            if target < value:
                right = index - 1
            else:
                left = index + 1
    return False


class TestSearch2DMatrix(unittest.TestCase):
    """
    Test Case for 2D Matrix
    """
    def test_one(self):
        """
        input = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
        target = 3
        """
        # arrange
        matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
        target = 3
        expecting = True

        # action
        result = search_2d_matrix(matrix, target)

        # assert
        assert result == expecting, f"expecting {expecting}, got {result}"

    def test_second(self):
        """
        Second Test
        matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
        """
        # arrange
        matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
        target = 13
        expecting = False

        # action
        result = search_2d_matrix(matrix, target)

        # assert
        assert result == expecting, f"expecting {expecting}, got {result}"


if __name__ == "__main__":
    unittest.main()
