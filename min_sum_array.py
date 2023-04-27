import unittest

def min_sum_array(nums, target):
    """
    min subarray greater than equals target
    """
    min_length = float('+Inf')
    left, right, acc = 0, 0, 0
    while right < len(nums) and left <= right:
        acc += nums[right]
        if acc >= target:
            while acc >= target:
                distance = right - left + 1
                min_length = min(min_length, distance)
                acc = acc - nums[left]
                left += 1
        right += 1
    if min_length <= len(nums):
        return min_length
    return 0


class MinSubArrayTest(unittest.TestCase):
    """
    Min SubArray Test Cases
    """

    def test_valid_case(self):
        """
        Test Valid Case
        """
        # arrange
        nums = [2, 3, 1, 2, 4, 3]
        target = 7
        expecting = 2

        # action
        result = min_sum_array(nums, target)

        # assert
        assert result == expecting, f"expecting {expecting}, got {result}"

    def test_invalid_case(self):
        """
        Test Invalid Case
        """
        # arrange
        nums = [1, 1, 1, 1, 1]
        target = 11
        expecting = 0

        # action
        result = min_sum_array(nums, target)

        # assert
        assert result == expecting, f"expecting {expecting}, got {result}"

    def test_full_length_valid_case(self):
        """
        Test Full Length Valid Case
        """
        # arrange
        nums = [1, 2, 3, 4, 5]
        target = 15
        expecting = 5

        # action
        result = min_sum_array(nums, target)

        # assert
        assert result == expecting, f"expecting {expecting}, got {result}"


if __name__ == "__main__":
    unittest.main()
