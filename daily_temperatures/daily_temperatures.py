import unittest


def daily_temperatures(temperatures):
    """
    receive and array of temperatures and 
    looks for a warm value forward
    """
    stack = []
    for index, temperature in enumerate(temperatures):
        while len(stack) > 0 and stack[-1][1] < temperature:
            left = stack.pop()
            temperatures[left[0]] = index - left[0]
        stack.append((index, temperature))
    while len(stack) > 0:
        temperatures[stack.pop()[0]] = 0
    return temperatures


class TestDailyTemperatures(unittest.TestCase):
    """
    Test Daily Temperatures
    """

    def test_example_1(self):
        """
        input = [73, 74, 75, 71, 69, 72, 76, 73]
        """
        # arrange
        temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
        expected = [1, 1, 4, 2, 1, 1, 0, 0]

        # action
        result = daily_temperatures(temperatures)

        # assert
        assert result == expected, f"expecting {expected}, got {result}"

    def test_example_2(self):
        """
        input = [30, 40, 50, 60]
        """
        # arrange
        temperatures = [30, 40, 50, 60]
        expected = [1, 1, 1, 0]

        # action
        result = daily_temperatures(temperatures)

        # assert
        assert result == expected, f"expecting {expected}, got {result}"

    def test_example_3(self):
        """
        input = [30, 60, 90]
        """
        # arrange
        temperatures = [30, 60, 90]
        expected = [1, 1, 0]

        # action
        result = daily_temperatures(temperatures)

        # assert
        assert result == expected, f"expecting {expected}, got {result}"


if __name__ == "__main__":
    unittest.main()
