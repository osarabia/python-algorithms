import unittest

def subarray_sum_equals(nums, k):
    """
    all subarray where sums equal to k
    """
    subarrays = 0
    current_sum = 0
    prefix_sum = {0: 1}

    for number in nums:
        current_sum += number
        diff = current_sum - k
        subarrays += prefix_sum.get(diff, 0)
        prefix_sum[current_sum] = 1 + prefix_sum.get(current_sum, 0)

    return subarrays


class TestSubArraySumEquals(unittest.TestCase):
    """
    Sub Array Sums Equals
    """

    def test_positive_same_values(self):
        """
        test all positives
        """
        # arrange
        numbers = [1, 1, 1]
        k = 2
        expected = 2

        # action
        result = subarray_sum_equals(numbers, k)

        # assert
        assert result == expected, f"expecting {expected}, got {result}"

    def test_some_negatives(self):
        """
        test some negatives
        """
        # arrange
        numbers = [-1, -1, 1]
        k = 0
        expecting = 1

        # action
        result = subarray_sum_equals(numbers, k)

        # assert
        assert result == expecting, f"expecting {expecting}, got {result}"
    
    def test_sum_everything(self):
        """
        test sum all the elements
        """
        # arrange
        numbers = [28, 54, 7, -70, 22, 65, -6]
        k = 100
        expecting = 1

        # action
        result = subarray_sum_equals(numbers, k)

        # assert
        assert result == expecting, f"expecting {expecting}, got {result}"


if __name__ == "__main__":
    unittest.main()