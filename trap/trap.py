import unittest


def trap(height):
    """
    total trap water extra space solution
    """
    total_area = 0
    max_left = [0] * len(height)
    max_right = [0] * len(height)

    for i in range(0, len(height)):
        if i > 0:
            max_left[i] = max(max_left[i-1], height[i-1])
        else:
            max_left[i] = 0
    
    for j in range(len(height)-1, -1, -1):
        if j < len(height) - 1:
            max_right[j] = max(max_right[j+1], height[j+1])
        else:
            max_right[j] = 0

    for k, value in enumerate(height):
        area = min(max_left[k], max_right[k]) - value
        if area > 0:
            total_area += area
    return total_area


def trap_no_extra_space(heights):
    """
    Test no extra space
    """
    total_area = 0
    left, right = 0, len(heights) - 1
    max_left, max_right = heights[left], heights[right]

    while left < right:
        if heights[left] <= heights[right]:
            left += 1
            area = min(max_left, max_right) - heights[left]
        else:
            right -= 1
            area = min(max_left, max_right) - heights[right]
        if area > 0:
            total_area += area
        max_left = max(max_left, heights[left])
        max_right = max(max_right, heights[right])

    return total_area


class TestTrap(unittest.TestCase):
    """
     Test Trap Water
    """
    def test_example_1(self):
        """Test example 1"""
        # arrange
        heights = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
        expected = 6

        # action
        result = trap(heights)

        # assert
        assert result == expected, f"expecting {expected}, got {result}"

    def test_example_2(self):
        """Test Example 2"""
        # arrange
        height = [4, 2, 0, 3, 2, 5]
        expected = 9

        # action
        result = trap(height)

        # assert
        assert result == expected, f"expecting {expected}, got {result}"

    def test_example_1_no_extra_space(self):
        """Test example 1"""
        # arrange
        heights = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
        expected = 6

        # action
        result = trap_no_extra_space(heights)

        # assert
        assert result == expected, f"expecting {expected}, got {result}"

    def test_example_2_no_extra_space(self):
        """Test Example 2"""
        # arrange
        height = [4, 2, 0, 3, 2, 5]
        expected = 9

        # action
        result = trap_no_extra_space(height)

        # assert
        assert result == expected, f"expecting {expected}, got {result}"


if __name__ == "__main__":
    unittest.main()
