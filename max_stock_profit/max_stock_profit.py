import unittest


def max_profit(stock):
    """
    Retrieve max stock profit extra space solution
    """

    max_right = [0] * len(stock)
    max_value = 0

    for j in range(len(stock) - 2, -1, -1):
        max_right[j] = max(max_right[j+1], stock[j+1])

    for i, value in enumerate(stock):
        diff = max_right[i] - value
        max_value = max(max_value, diff)

    return max_value


def max_profit_no_extra_space(stock):
    """
    Test max profit no extra space
    """
    left, right = 0, 1
    max_value = 0

    while left < right and right < len(stock):
        if stock[left] >= stock[right]:
            left = right
            right = right + 1
        else:
            diff = stock[right] - stock[left]
            right += 1
            max_value = max(max_value, diff)
    return max_value


class TestMaxProfit(unittest.TestCase):
    """
    Test Max Profit
    """

    def test_example_1(self):
        """
        Test Example 1
        """
        # arrange
        stock = [7, 1, 5, 3, 6, 4]
        expected = 5

        # action
        result = max_profit(stock)

        # assert
        assert result == expected, f"expecting {expected}, got {result}"

    def test_example_2(self):
        """
        Test Example 2
        """
        # arrange
        stock = [7, 6, 4, 3, 1]
        expected = 0

        # action
        result = max_profit(stock)

        # assert
        assert result == expected, f"expecting {expected}, got {result}"

    def test_example_no_extra_1(self):
        """
        Test Example 1 no extra space solution
        """
        # arrange
        stock = [7, 1, 5, 3, 6, 4]
        expected = 5

        # action
        result = max_profit_no_extra_space(stock)

        # assert
        assert result == expected, f"expecting {expected}, got {result}"

    def test_example_no_extra_2(self):
        """
        Test Example 2 no extra space solution
        """
        # arrange
        stock = [7, 6, 4, 3, 1]
        expected = 0

        # action
        result = max_profit_no_extra_space(stock)

        # assert
        assert result == expected, f"expecting {expected}, got {result}"

    def test_example_no_extra_3(self):
        """
        Test Example 3 no extra space solution
        """
        # arrange
        stock = [7, 6, 4, 1, 20]
        expected = 19

        # action
        result = max_profit_no_extra_space(stock)

        # assert
        assert result == expected, f"expecting {expected}, got {result}"


if __name__ == "__main__":
    unittest.main()
