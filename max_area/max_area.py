import unittest


def max_area(heights):
    """
    Return the max are of an array of heights
    """
    left, right = 0, len(heights) - 1
    area = min(heights[left], heights[right]) * (right - left)
    while left < right:
        if heights[left] <= heights[right]:
            left += 1
        else:
            right -= 1
        calculated_area = min(heights[left], heights[right]) * (right - left)
        area = max(area, calculated_area)

    return area


class TestMaxArea(unittest.TestCase):
    """
    Test for Max area
    """

    def test_long_distance(self):
        """
        Test long distance between left and right
        """
        # arrange
        array = [1, 8, 6, 2, 5, 4, 8, 3, 8]
        expected = 56

        # action
        result = max_area(array)

        # assert
        assert result == expected, f"expecting {expected}, got {result}"

    def test_max_height_at_each_other(self):
        """
        max height at each other
        """
        # arrange
        array = [1, 8, 6, 49, 49, 1, 2, 3, 5]
        expected = 49

        # action
        result = max_area(array)

        # assert
        assert result == expected, f"expecting {expected}, got {result}"


if __name__ == "__main__":
    unittest.main()
