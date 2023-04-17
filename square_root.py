import unittest

def no_no_square_root(number):
    """
    Given an integer, finds its square root w/o using built-in square root function.
    Only return the integert part (truncate decimals)
    """
    square_root = 0
    left, right = 0, number

    while left <= right:
        mid = (right + left) // 2
        if mid * mid < number:
            square_root = mid
            left = mid + 1
        elif mid * mid == number:
            return mid
        else:
            right = mid - 1

    return square_root


class TestNoSquareRoot(unittest.TestCase):
    """
    Test no no square root
    """

    def test_exact_match(self):
        """
        first test
        """
        # arrange
        number = 16
        expecting = 4
        # action
        result = no_no_square_root(number)
        # assert
        assert result == expecting, f"expecting {expecting}, got {result}"

    def test_no_exact_match(self):
        """
        test no exact match
        """
        # arrange
        number = 8
        expecting = 2

        # action
        result = no_no_square_root(number)

        # assert
        assert result == expecting, f"expecting {expecting}, got {result}"


if __name__ == "__main__":
    unittest.main()
