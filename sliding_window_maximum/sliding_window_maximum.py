import unittest
import collections


def max_sliding_window(nums, k):
    """
    Sliding Window Maximum
    """
    if k == 1:
        return nums
    output = []
    queue = collections.deque()
    left = right = 0

    while right < len(nums):
        while len(queue) > 0 and nums[queue[-1]] < nums[right]:
            queue.pop()
        queue.append(right)
        distance = right - left + 1
        if distance == k:
            output.append(nums[queue[0]])
            left += 1
            if left > queue[0]:
                queue.popleft()
        right += 1
    return output


class TestSlidingWindowMax(unittest.TestCase):
    """
    Test for Sliding Window Max
    """
    def test_example_1(self):
        """
        Example 1:
        nums = [1,3,-1,-3,5,3,6,7]
        k = 3
        """
        # arrange
        nums = [1, 3, -1, -3, 5, 3, 6, 7]
        k = 3
        expected = [3, 3, 5, 5, 6, 7]

        # action
        result = max_sliding_window(nums, k)

        # assert
        assert result == expected, f"expecting {expected}, got {result}"

    def test_example_2(self):
        """
        Example 2:
        nums = [-7,-8,7,5,7,1,6,0]
        k = 4
        """
        # arrange
        nums = [-7, -8, 7, 5, 7, 1, 6, 0]
        k = 4
        expected = [7, 7, 7, 7, 7]

        # action
        result = max_sliding_window(nums, k)

        # assert
        assert result == expected, f"expecting {expected}, got {result}"

    def test_example_3(self):
        """
        Test Example 3:
        nums = [7,2,4]
        k = 2
        """
        # arrange
        nums = [7, 2, 4]
        k = 2
        expected = [7, 4]

        # action
        result = max_sliding_window(nums, k)

        # assert
        assert result == expected, f"expecting {expected}, got {result}"

    def test_example_4(self):
        """
        test example 4:
        nums = [1, 3, 1, 2, 0, 5]
        k = 3
        """
        # arrange
        nums = [1, 3, 1, 2, 0, 5]
        k = 3
        expected = [3, 3, 2, 5]

        # action
        result = max_sliding_window(nums, k)

        # assert
        assert result == expected, f"expecting {expected}, got {result}"


if __name__ == "__main__":
    unittest.main()
