import unittest


def product_of_array_except_self(nums):
    """
    Product of all element of array except self
    """
    left = len(nums) * [1]
    right = len(nums) * [1]

    for i in range(1, len(nums)):
        if i == 1:
            left[i] = nums[i-1]
        else:
            left[i] = nums[i-1] * left[i-1]

    for j in range(len(nums)-2, -1, -1):
        if j == len(nums) - 2:
            right[j] = nums[j+1]
        else:
            right[j] = nums[j+1] * right[j+1]

    for k, _ in enumerate(nums):
        nums[k] = left[k] * right[k]
    return nums


class TestProductOfArrayExceptSelf(unittest.TestCase):
    """
    Test Product of Array Except Self
    """

    def test_example_1(self):
        """
        First Example
        array = [1, 2, 3, 4]
        expected = [24, 12, 8, 6]
        """
        # arrange
        array = [1, 2, 3, 4]
        expected = [24, 12, 8, 6]
        # action
        resp = product_of_array_except_self(array)
        # assert
        assert resp == expected, f"expecting {expected}, got {resp}"

    def test_example_2(self):
        """
        Second Example
        array = [-1,1,0,-3,3]
        expected = [0,0,9,0,0]
        """
        # arrange
        array = [-1, 1, 0, -3, 3]
        expected = [0, 0, 9, 0, 0]

        # action
        resp = product_of_array_except_self(array)

        # assert
        assert resp == expected, f"expecting {expected}, got {resp}"


if __name__ == "__main__":
    unittest.main()
